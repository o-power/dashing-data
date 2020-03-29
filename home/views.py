from django.shortcuts import render, get_object_or_404, redirect, reverse
from subscription.models import SubscriptionType

def index(request):
    """
    A view that displays the index page.
    """
    subscription_types = SubscriptionType.objects.all().order_by('length_months')

    return render(request, 'home/index.html', {'subscription_types': subscription_types})

def create_chart(request):
    """
    A view that lists the available chart types.
    """
    return render(request, 'home/createchart.html')