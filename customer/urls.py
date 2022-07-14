from django.urls import path
from .views import signup,profile,edit_profile
from django.contrib.auth import views

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    path('login/', views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]