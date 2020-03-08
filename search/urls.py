from django.urls import path
from django.views.generic.base import RedirectView
from .views import all_charts, do_search, save_chart

urlpatterns = [
    path('', RedirectView.as_view(url='charts/')),
    path('charts/', all_charts, name='all_charts'),
    path('result/', do_search, name='do_search'),
    path('save/', save_chart, name='save_chart'),
]