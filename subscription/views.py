from django.shortcuts import render
from .models import SubscriptionType

def choose_subscription(request):
    """"""
    subscription_types = SubscriptionType.objects.all().order_by('length_months')
    return render(request, 'subscription/subscriptions.html', {'subscription_types': subscription_types})