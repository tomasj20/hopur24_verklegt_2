from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='staff-index'),
    path('customerView', views.customerView, name='customerView'),
    path('<int:id>', views.get_cereal_by_id, name='admin-cereal-details'),
    path('create_cereal_start', views.create_cereal_start, name="create_cereal_start"),
    path('create_cereal2',views.create_cereal2, name="create_cereal2"),
    path('delete_cereal/<int:id>', views.delete_cereal, name='delete_cereal'),
    path('update_cereal/<int:id>', views.update_cereal, name='update_cereal'),
    path('productlist', views.get_product_list, name='productlist'),
]
