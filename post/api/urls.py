from django.urls import path
from . import views

urlpatterns= [
    path('create/', views.PostCreateAPIView.as_view(),name='postcreate-api'),
    path('postlist/', views.PostListAPIView.as_view(), name='postlist-api' ),
    path('<slug>/', views.PostDetailAPIView.as_view(), name='postdetail-api' ),
    ]