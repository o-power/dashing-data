from django.urls import path
from .views import index, create_chart

app_name = 'home'
urlpatterns = [
    path('', index, name='index'),
    path('charts/', create_chart, name='create_chart'),
]