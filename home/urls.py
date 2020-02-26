from django.urls import path
from .views import index, create_chart

urlpatterns = [
    path('', index, name='index'),
    path('charts/', create_chart, name='create_chart'),
]