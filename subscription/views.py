from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import SubscriptionType, UserSubscription
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required
def choose_subscription(request):
    """ """
    subscription_types = SubscriptionType.objects.all().order_by('length_months')

    # dependent on there being only one subscription per user!
    try:
        user_subscription = UserSubscription.objects.get(user_id=request.user.id)
    except UserSubscription.DoesNotExist:
        user_subscription = None

    if user_subscription:
        end_date = user_subscription.end_date
        if end_date > timezone.now():
            messages.warning(request, "You have an active subscription until {0}".format(
                timezone.localtime(end_date).strftime("%d %b, %Y at %H:%M:%S")))
        else:
            messages.info(request, "Your subscription expired on {0}".format(
                timezone.localtime(end_date).strftime("%d %b, %Y at %H:%M:%S")))

    return render(request, 'subscription/subscriptions.html', {'subscription_types': subscription_types})

@login_required
def pay_subscription(request, pk=None):
    """ """
    
    subscription_type = get_object_or_404(SubscriptionType, pk=pk) if pk else None
    
    # dependent on there being only one subscription per user!
    try:
        existing_user_subscription = UserSubscription.objects.get(user_id=request.user.id)
    except UserSubscription.DoesNotExist:
        existing_user_subscription = None

    # if the user has an active subscription, redirect them away
    if existing_user_subscription:
        existing_end_date = existing_user_subscription.end_date
        if existing_end_date > timezone.now():
            messages.error(request, "You have an active subscription that expires on {0}".format(
                    timezone.localtime(existing_end_date).strftime("%d %b, %Y at %H:%M:%S")))
            return redirect(reverse('search:all_charts'))
    
    if request.method == 'POST':
        #print(request.POST.keys())
        #dict_keys(['csrfmiddlewaretoken', 'stripeToken'])
        # Token is created using Stripe Checkout or Elements!
        # Get the payment token ID submitted by the form:
        token = request.POST.get('stripeToken', False)

        if token:
            try:
                charge = stripe.Charge.create(
                    amount=int(subscription_type.price*100),
                    currency='eur',
                    description=request.user.email,
                    source=token,
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if charge.paid:
                # python manage.py shell
                # from django.utils import timezone
                # start_date = timezone.now()
                start_date = timezone.now()
                end_date = start_date + relativedelta(months=+subscription_type.length_months)

                if existing_user_subscription:
                    existing_user_subscription.subscription_type_id = subscription_type
                    existing_user_subscription.start_date = start_date
                    existing_user_subscription.end_date = end_date
                    existing_user_subscription.save()
                else:   
                    user_subscription = UserSubscription(
                        user_id = request.user,
                        subscription_type_id = subscription_type, 
                        start_date = start_date,
                        end_date = end_date
                    )
                    user_subscription.save()

                messages.error(request, "You have successfully paid for {0} months".format(subscription_type.length_months))
                return redirect(reverse('search:all_charts'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    return render(request, 'subscription/payment.html', { 'publishable': settings.STRIPE_PUBLISHABLE, 'subscription_type': subscription_type})