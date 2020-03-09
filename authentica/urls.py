from django.urls import path
from . import views

urlpatterns= [
path('register/', views.RegisterView.as_view(), name='register'),
path('', views.index, name='home'),
path('logout/', views.logout_view, name='logout'),
path('login/', views.LoginView.as_view(), name='login'),
path('profile/', views.UserView.as_view(), name= 'user'),
# path('profile/', views.UserProfileUpdate.as_view(), name= 'user')
]