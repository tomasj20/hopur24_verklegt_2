from django.urls import path
from . import views

urlpatterns = [
    path('healthy',views.healthyIndex, name='healthy'),
    path('sugary',views.sugaryIndex, name='sugary'),
    path('vegan',views.veganIndex, name='vegan')
]