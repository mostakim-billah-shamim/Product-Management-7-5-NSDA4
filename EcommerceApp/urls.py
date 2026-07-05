from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardPage, name='dashboard'),


    path('register/', RegisterPage, name='register'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutPage, name='logout'),


    path('profile/', ProfilePage, name='profile'),
    path('createprofile-ad/', AdminProfilePage, name='createprofile_ad'),
    path('createprofile-cu/', CustomerProfilePage, name='createprofile_cu'),


    path('category/', categorypage, name='category'),
    path('editCategory/<str:id>/', categoryEditpage, name='editCategory'),
    path('delCategory/<str:id>/', CategoryDeletePage, name='delCategory'),


    path('product/', ProductPage, name='product'),
    path('editProduct/<str:id>/', ProductPage, name='editProduct'),
    path('delProduct/<str:id>/', ProductDeletePage, name='delProduct'),
]