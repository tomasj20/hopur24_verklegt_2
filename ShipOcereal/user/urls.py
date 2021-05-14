from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', LoginView.as_view(template_name='user/login/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profilemenu', views.profile_menu, name='profilemenu'),
    path('profileinfo', views.profile_info, name='profileinfo'),
    path('profile', views.profile, name='profile'),
    path('search_history', views.search_history, name="search_history")
]