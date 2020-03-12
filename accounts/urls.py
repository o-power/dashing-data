from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import register, profile, logout, login
from . import urls_reset

app_name = 'accounts'
urlpatterns = [
    path('', RedirectView.as_view(url='register/')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('password-reset/', include(urls_reset)),
]