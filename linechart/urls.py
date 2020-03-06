from django.urls import path
from .views import upload_line_chart

app_name = 'linechart'
urlpatterns = [
    path('upload/', upload_line_chart, name='upload_line_chart'),
]