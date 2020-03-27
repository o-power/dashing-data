from django.db import models
from django.contrib.auth.models import User

class UserChart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chart_type = models.CharField(max_length=50)
    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "user_id: " + str(self.user_id) + \
            " chart_id: " + str(self.pk)

class BarChart(models.Model):
    chart_id = models.ForeignKey(UserChart, on_delete=models.CASCADE)
    x_data = models.CharField(max_length=50)
    y_data = models.DecimalField(max_digits=14, decimal_places=5)

    def __str__(self):
        return " chart_id: " + str(self.chart_id) + \
            " row_id: " + str(self.pk)

class LineChart(models.Model):
    chart_id = models.ForeignKey(UserChart, on_delete=models.CASCADE)
    x_data = models.CharField(max_length=50)
    y_data = models.DecimalField(max_digits=14, decimal_places=5)

    def __str__(self):
        return " chart_id: " + str(self.chart_id) + \
            " row_id: " + str(self.pk)