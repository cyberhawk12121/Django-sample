from django.urls import path
from . import views

urlpatterns= [
    path('create/', views.PostCreate.as_view(), name='createpost' ),
    path('<slug:slug_url>', views.PostDetail.as_view(), name= 'postdetail'),
    path('postlist/', views.PostList.as_view(), name='postlist'),
    path('', views.likeToggle, name= 'like'),
    path('edit/<slug:slug_url>', views.PostEdit.as_view(), name= 'edit')
]