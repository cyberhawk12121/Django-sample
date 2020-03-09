from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView, 
    View, 
    CreateView, 
    DeleteView, 
    DetailView, 
    ListView,
    UpdateView,
    )
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Profile


def index(request):
    if not request.user.is_authenticated:
        redirect('login')
    user= CustomUser.objects.all()
    return render(request, 'authentica/index.html', {'user': user})


class RegisterView(TemplateView):
    template_name= 'authentica/register.html'
    def get(self, request):
        user= request.user
        if user.is_authenticated:
            return redirect('home')
        else:
            form = RegisterForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                instance= form.save(commit=False)
                instance.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password2')
                avatar= form.cleaned_data.get('avatar')
                print(password)
                print(email)
                print(avatar)
                user = authenticate(email=email ,password=password) #django built in authentication
                login(request, user)
                return redirect('home') 
        else:
            form = RegisterForm()
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    template_name= 'authentica/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form= LoginForm()
            return render(request, self.template_name, {'form': form})
    def post(self, request):
        if request.POST:
            form= LoginForm(request.POST)
            if form.is_valid():
                email= form.cleaned_data.get('email')
                password= form.cleaned_data.get('password')
                print(email, password)
                user= authenticate(email= email, password= password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {email}")
                    return redirect('home')
        else:
            form= LoginForm()
        return render(request, self.template_name, {'form':form})


class UserView(LoginRequiredMixin ,TemplateView):
    template_name= 'authentica/user_profile.html'

# class UserProfileUpdate(UpdateView):
#     model= Profile
#     fields= ['avatar', 'bio']


def logout_view(request):
    if request.POST:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')

