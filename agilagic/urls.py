"""agilagic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls.py/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('user_authentication.urls')),
    path(r'', include('financial_transaction.urls')),
    path(r'', include('products_transaction.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'user_authentication.views.error404_view'
