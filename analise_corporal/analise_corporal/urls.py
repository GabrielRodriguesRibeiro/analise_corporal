"""
URL configuration for analise_corporal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from cadastro_usuario import views as cadastro_views
from corpo import views as corpo_views

urlpatterns = [
    path('', cadastro_views.login_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', cadastro_views.login_view, name='login'),
    path('formulario_corpo/',  corpo_views.formulario_corpo_view, name='formulario_corpo'),
]
