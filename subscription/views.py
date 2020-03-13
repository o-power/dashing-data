from django.shortcuts import render, get_object_or_404
from .models import SubscriptionType
from .forms import MakePaymentForm
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
    print(subscription_type.name)
    print(subscription_type.description)
    print(subscription_type.length_months)
    print(subscription_type.price)

    payment_form = MakePaymentForm()

    # need to stop user paying twice - maybe in profile?

    return render(request, 'subscription/payment.html', {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})