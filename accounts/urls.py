from django.urls import path
from .views import register, profile, logout, login

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    #url(r'^password-reset/', include(urls_reset)),
]