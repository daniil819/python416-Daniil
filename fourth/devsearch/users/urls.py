from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.user_profile, name='user_profile'),
    # Регистрция и авторизация
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
