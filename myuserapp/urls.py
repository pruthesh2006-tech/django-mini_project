from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('add-category/', views.add_category, name='add_category'),
    path('display-category/', views.display_category, name='display_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit_product'),
    path('product/', views.product, name='product'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('editproduct/<int:id>/', views.editproduct, name='editproduct'),
    path('updateproduct/<int:id>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:id>/', views.deleteproduct, name='deleteproduct'),

    path('login_view/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('user_home/', views.user_home_view, name='user_home'),
    path('logout/', views.logout_view, name='logout'),
]