"""
URL configuration for hopetrade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from sesiones import views as sesiones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sesiones/', include(('sesiones.urls', 'sesiones'))),
    path('publicaciones/', include(('publicaciones.urls', 'publicaciones'))),
    path('intercambios/', include(('intercambios.urls', 'intercambios'))),
    path('listados/', include(('listados.urls', 'listados'))),
    path('', sesiones.ver_landing_page),
    path('ofrecimientos/', include('ofrecimientos.urls')),
    path('historiales/', include(('historiales.urls', 'historiales'))),
    path('estadisticas/', include(('estadisticas.urls', 'estadisticas'))),
    path('donaciones/', include(('donaciones.urls', 'donaciones')))
]
