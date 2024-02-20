from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user_login/',views.user_login,name='user_login'),
    # path('logout/', views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('home2/',views.home2,name="home2")
    # Add more URL patterns as needed
]
