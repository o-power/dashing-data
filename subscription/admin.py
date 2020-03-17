from django.contrib import admin
from .models import SubscriptionType, UserSubscription

admin.site.register(SubscriptionType)
admin.site.register(UserSubscription)