from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.github_profile, name='github_profile'),
]