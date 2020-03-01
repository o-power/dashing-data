from django.urls import path
from .views import save_chart

urlpatterns = [
    path('', save_chart, name='save_chart')
]