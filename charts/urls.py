from django.conf.urls import url
from .views import create_bar_chart

urlpatterns = [
    url(r'^$', create_bar_chart, name='create_bar_chart'),
]