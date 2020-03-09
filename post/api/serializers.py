from rest_framework.serializers import ModelSerializer
from post.models import Posts

class PostSerializer(ModelSerializer):
    class Meta:
        model= Posts
        fields= [
            'author',
            'id',
            'title',
            'slug',
            'content',
        ]

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model= Posts
        fields= [
            'author',
            # 'id',
            'title',
            # 'slug',
            'content',
        ]
