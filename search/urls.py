from django.urls import path
from .views import save_chart, all_charts

urlpatterns = [
    path('', all_charts, name='all_charts'),
    path('save/', save_chart, name='save_chart'),
]