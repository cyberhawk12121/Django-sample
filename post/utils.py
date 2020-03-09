from django.utils.text import slugify
from .models import Posts
def unique_slug_generator(model_instance, title, sluf_field):
    slug= slugify(title)
    model_class= model_instance.__class__
    while model_class._default_manager.filter(slug=slug).exists():
        # Posts.objects.filter(slug=slug).exists()
        object_pk= model_class._default_manager.latest('pk')
        object_pk=object_pk.pk+1
        
        slug= f'{slug}-{object_pk}'
    return slug