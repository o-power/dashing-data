from django.shortcuts import render

def choose_subscription(request):
    """"""
    return render(request, 'subscription/subscriptions.html')