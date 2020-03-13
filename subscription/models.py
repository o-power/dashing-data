from django.db import models
from django.contrib.auth.models import User

class SubscriptionType(models.Model):
    description = models.CharField(max_length=50, blank=False)
    length_months = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

# class UserSubscription(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     start_date = models.DateTimeField(blank=False)
#     end_date = models.DateTimeField(blank=False)

#     def __str__(self):
#         return "user_id: " + str(self.user_id) + \
#             " subscription_id: " + str(self.pk)