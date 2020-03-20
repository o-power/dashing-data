"""dashing_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import urls as urls_home
from accounts import urls as urls_accounts
from search import urls as urls_search
from barchart import urls as urls_barchart
from linechart import urls as urls_linechart
from subscription import urls as urls_subscription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls_home)),
    path('accounts/', include(urls_accounts)),
    path('search/', include(urls_search)),
    path('barchart/', include(urls_barchart)),
    path('linechart/', include(urls_linechart)),
    path('subscription/', include(urls_subscription))
]

# Django does not serve media files in DEBUG mode
if settings.DEBUG and not settings.USE_S3:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)