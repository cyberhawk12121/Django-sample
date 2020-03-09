from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from .models import CustomUser, Profile
 

class RegisterForm(UserCreationForm):
    # avatar= forms.ImageField(widget= forms.I)
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(forms.Form):
    email= forms.CharField(max_length=255, widget= forms.EmailInput)
    password= forms.CharField(max_length=255, widget=forms.PasswordInput)
    
class ProfileForm(forms.Form):
    avatar= forms.ImageField(label=None, widget=forms.FileInput(attrs={'class':'form-control'}))
    bio= forms.CharField(label= None ,widget= forms.Textarea(attrs={'class':'bio-style form-control'}))
    class Meta:
        models= Profile
        fields= ('avatar', 'bio')
