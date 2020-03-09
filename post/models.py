from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from authentica.models import CustomUser
from django.utils import timezone
from django.utils.text import slugify
from django import forms
from django.urls import reverse
from django.db.models.signals import pre_save
# from .utils import unique_slug_generator


# Creating validator for the following model
def validate_for_empty(value):
    pass

class Posts(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    likes= models.ManyToManyField(settings.AUTH_USER_MODEL, blank= True, related_name='likes')
    published_time= models.DateTimeField(auto_now_add=True, blank=True)
    title= models.CharField(blank=False, editable=True, max_length=255)
    slug= models.SlugField(max_length=255, blank= True, null= True,allow_unicode=True, unique= True)
    updated= models.DateTimeField(auto_now=True, blank= True)
    content= models.CharField(default=False, max_length=10000,editable=True)
    
    def get_absolute_url(self): 
        return reverse(
            'postdetail',
            kwargs={'slug': self.slug}) 

    def get_like_url(self):
        return reverse('like', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

# SLUGS Generator
def create_slug(instance, new_slug=None):
    slug= slugify(instance.title)
    if new_slug is not None:
        slug= new_slug
    qs= Posts.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists:
        new_slug="%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug= create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Posts)
