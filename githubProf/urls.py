from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_view, name='search'),
    path('profile/<str:username>/', views.github_profile, name='github_profile'),
]