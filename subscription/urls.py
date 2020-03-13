from django.urls import path, include
from .views import choose_subscription, pay_subscription

app_name = 'subscription'
urlpatterns = [
    path('', choose_subscription, name='choose_subscription'),
    path('<int:pk>/payment/', pay_subscription, name='pay_subscription'),
]