"""ShipOcereal URL Configuration

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
from django.urls import path
from django.conf.urls import include
from home.models import Cereal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('staff.urls')),
    path('',include('home.urls')),
    path('filter/',include('filter.urls')),
    path('cart/',include('cart.urls')),
    path('<int:id>',include('home.urls')),
    path('create_cereal/', include('home.urls')),
    path('create_cereal2/',include('home.urls')),
    path('update_cereal', include('home.urls')),
    path('user/', include('user.urls')),
    path('update_item', include('user.urls')),
    path('paymentstep1',include('cart.urls')),
    path('paymentstep2',include('cart.urls')),
    path('paymentstep3',include('cart.urls'))
]
