from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import SubscriptionType
#from .forms import MakePaymentForm
from django.contrib import messages
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET

def choose_subscription(request):
    """ """
    subscription_types = SubscriptionType.objects.all().order_by('length_months')
    return render(request, 'subscription/subscriptions.html', {'subscription_types': subscription_types})

def pay_subscription(request, pk=None):
    """ """
    
    subscription_type = get_object_or_404(SubscriptionType, pk=pk) if pk else None
    
    print('Make payment')
    #print(subscription_type.name)
    #print(subscription_type.description)
    #print(subscription_type.length_months)
    #print(subscription_type.price)

    #payment_form = MakePaymentForm()

    # need to stop user paying twice - maybe in profile?

    #'payment_form': payment_form,

    if request.method == 'POST':
        #print(request.POST.keys())
        #dict_keys(['csrfmiddlewaretoken', 'stripeToken'])
        # Token is created using Stripe Checkout or Elements!
        # Get the payment token ID submitted by the form:
        token = request.POST.get('stripeToken', False)

        if token:
            try:
                # user must be created to put this in description!
                charge = stripe.Charge.create(
                    amount=int(subscription_type.price*100),
                    currency='eur',
                    description=request.user.email,
                    source=token,
                )
                # go somewhere?
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if charge.paid:
                # flag user as paid using UserSubscription?
                messages.error(request, "You have successfully paid")
                return redirect(reverse('search:all_charts'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    return render(request, 'subscription/payment.html', { 'publishable': settings.STRIPE_PUBLISHABLE, 'subscription_type': subscription_type})