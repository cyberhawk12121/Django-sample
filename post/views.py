from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, Http404
from django.contrib.auth import login, authenticate, logout
from .forms import PostForm
from .models import Posts
from rest_framework import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, 
    View, 
    CreateView, 
    DeleteView, 
    DetailView, 
    ListView,
    FormView,
    RedirectView,
    UpdateView
    )
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.views.generic.edit import FormMixin


class PostCreate(LoginRequiredMixin ,TemplateView):
    template_name= 'post/bloginput.html'
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('postdetail')
        else:
            form= PostForm()
            return render(request, self.template_name, {'form':form})
    def post(self, request):
        if request.POST:
            form= PostForm(request.POST)
            if form.is_valid():
                # post= get_object_or_404(Posts)
                # print(post.title)
                content= form.cleaned_data.get('content')
                title= form.cleaned_data.get('title')
                print(content, title)
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                # date= Posts.objects.filter()
                return redirect('home')
        else:
            form= PostForm()

        return render(request, self.template_name, {'form':form})
        
class PostList(ListView):
    model= Posts
    template_name= 'post/posts_list.html'
    paginate_by= 6
    def get_queryset(self):
        try:
            post=Posts.objects.filter(published_time__lte=timezone.now()).order_by('-published_time')
        except post.DoesNotExist:
            raise Http404
        else:
            return post
class PostDetail(DetailView):
    model= Posts
    slug_url_kwarg= 'slug_url'
    slug_field= 'slug'
  
def likeToggle(request, *args,**kwargs):
    if request.POST:
        post= get_object_or_404(Posts, id= request.POST.get('post_id'))
        string= str(post)
        s= string.lower()
        st= s.replace(" ","-")
        print(st)
        user= request.user
        print(user)
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
    else:
        return redirect('login')
    return redirect(request.META.get('HTTP_REFERER'))

class PostEdit(UpdateView):
    model= Posts
    fields= ['title', 'content']
    # post= get_object_or_404(Posts)
    # template_name= 'post/bloginput.html'
    slug_url_kwarg= 'slug_url'
    slug_field= 'slug'
    success_url= reverse_lazy('postlist')


# class PostDelete(DeleteView):
#     pass
