"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from web.views import indice, acerca, producto, user, carrito, contacto, exito, compra, reembolso, faq




urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',indice, name="indice"),
    path ('acerca', acerca, name="acerca"),
    path ('producto',producto, name="producto"),
    path ('user', user, name="user"),
    path ('carrito', carrito, name='carrito'),
    path ('contacto', contacto, name='contacto'),
    path ('exito', exito, name='exito'),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('compra', compra, name='compra'),
    path ('reembolso', reembolso, name='reembolso'),
    path ('faq', faq, name='faq'),
    
]
