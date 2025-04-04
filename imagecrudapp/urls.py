from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('showproduct',views.showproduct,name='showproduct'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct'),
    path('delete/<int:pk>',views.delete,name='delete'),






]