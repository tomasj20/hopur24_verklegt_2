from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('cart', views.index, name='cart'),
    path('paymentstep1',views.paymentStep1,name='paymentstep1'),
    path('paymentstep2',views.paymentStep2,name='paymentstep2'),
    path('paymentstep3',views.paymentStep3,name='paymentstep3')
]