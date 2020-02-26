from django.urls import path
from .views import upload_bar_chart, create_bar_chart

urlpatterns = [
    path('upload', upload_bar_chart, name='upload_bar_chart'),
    path('chart', create_bar_chart, name='create_bar_chart'),
]