from django.urls import path
from django.views.generic.base import RedirectView
from .views import upload_line_chart#, create_line_chart

app_name = 'linechart'
urlpatterns = [
    path('', RedirectView.as_view(url='upload/')),
    path('upload/', upload_line_chart, name='upload_line_chart'),
    #path('chart/', create_line_chart, name='create_line_chart'),
]