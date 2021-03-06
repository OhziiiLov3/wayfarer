from main_app.models import Posts
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.UserProfileList.as_view(), name="profile_detail"),
    path('profile/<int:pk>/', views.UserProfileUpdate.as_view(), name="profile_update"),
    path('post/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]
