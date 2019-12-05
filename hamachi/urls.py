"""hamachi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import sushibar.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sushibar.views.home, name='home'),
    path('system/', sushibar.views.system, name='system'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('error/', sushibar.views.error, name='error'),
    path('reserva/', sushibar.views.reserva, name='reserva'),
    path('postulante/', sushibar.views.postulante, name='postulante'),
    path('mensaje/', sushibar.views.mensaje, name='mensaje'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
