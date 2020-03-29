from django.urls import path
from django.views.generic.base import RedirectView
from .views import upload_chart, create_chart, view_chart

app_name = 'linechart'
urlpatterns = [
    path('', RedirectView.as_view(url='upload/')),
    path('upload/', upload_chart, name='upload_chart'),
    path('chart/', create_chart, name='create_chart'),
    path('<int:pk>/view/', view_chart, name='view_chart'),
]