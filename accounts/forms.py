from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model
from .models import Book

#from django.contrib.auth.models import User

#User=get_user_model()

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'input100'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'input100'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username', 'class':'input100'}),
            'email': forms.TextInput(attrs={'placeholder':'Email', 'class':'input100'}),
        }
        
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'input100'}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'input100'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid Username or Password')
            if not user.check_password(password):
                raise forms.ValidationError('Wrong Password')
            if not user.is_active:
                raise forms.ValidationError('not active')
        return super(UserLoginForm, self).clean(*args, **kwargs) 


class BookForm(forms.ModelForm):
    class Meta:
        model=Book 
        fields=['title','author','pdf','category']

