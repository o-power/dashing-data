from django.urls import path
from django.views.generic.base import RedirectView
from .views import upload_bar_chart, create_bar_chart

app_name = 'barchart'
urlpatterns = [
    path('', RedirectView.as_view(url='upload/')),
    path('upload/', upload_bar_chart, name='upload_bar_chart'),
    path('chart/', create_bar_chart, name='create_bar_chart'),
]