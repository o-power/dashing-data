from django.shortcuts import render, redirect, reverse
from django.conf import settings
from subscription.models import UserSubscription

def upload_chart(request):
    """
    A form through which the user uploads data.
    If method is POST, save data in a session object.
    If method is GET, render an empty upload data form.
    """    
    # if the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('{0}?next={1}'.format(settings.LOGIN_URL, request.path))
    # else if user is logged in, check subscription
    else:
        try:
            user_subscription = UserSubscription.objects.get(user_id=request.user.id)
        except UserSubscription.DoesNotExist:
            user_subscription = None
    
        # a subscription is required to create this chart type
        if user_subscription is None:
            return redirect(reverse('subscription:choose_subscription'))
        # an expired subscription
        elif user_subscription.status == 'Expired':
            return redirect(reverse('subscription:choose_subscription'))

    return render(request, 'linechart/chart.html')

#def create_chart(request):
#    """
#    Render page with bar chart.
#    """
#    return render(request, 'linechart/chart.html')