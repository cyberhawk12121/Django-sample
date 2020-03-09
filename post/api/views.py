from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, PostCreateSerializer
from post.models import Posts

class PostCreateAPIView(CreateAPIView):
    queryset= Posts.objects.all()
    serializer_class= PostCreateSerializer

class PostUpdateAPIView(UpdateAPIView):
    queryset= Posts.objects.all()
    serializer_class= PostCreateSerializer
    lookup_field= 'slug'
    permission_classes= [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
class PostListAPIView(ListAPIView):
    # Takes :
    # 1. queryset
    # 2. serializer_class
    # 3. permissions_class
    queryset= Posts.objects.all()
    serializer_class= PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset= Posts.objects.all()
    serializer_class= PostSerializer
    lookup_field= 'slug'
    # lookup_url_kwarg= 'slug'