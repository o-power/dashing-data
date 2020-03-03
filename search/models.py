from django.db import models
from django.contrib.auth.models import User

class UserChart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chart_type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "user_id: " + str(self.user_id) + \
            " chart_id: " + str(self.pk)

#class BarChart(models.Model):
#    chart_id = models.ForeignKey(UserCharts, on_delete=models.CASCADE)
#    x_data = 
#    y_data = 