from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>', views.get_cereal_by_id, name='cereal-details'),
    path('create_cereal', views.create_cereal_start, name="create_cereal_start"),
    path('create_cereal2',views.create_cereal, name="create_cereal"),
    path('delete_cereal/<int:id>', views.delete_cereal, name='delete_cereal'),
    path('update_cereal', views.update_cereal, name="update_cereal"),
    path('update_item', views.updateItem, name="updateItem"),
]