from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# UserRegisterForm is inherited from usercreationform

class UserRegisterForm(UserCreationForm):
#email field created by us , rest are in-built
    email = forms.EmailField(max_length=100,help_text='Enter a valid email address')
# similar to -> <input type='email' name='email' max=100>
# meta class always defined inside another class
# used to define the model connected to superclass and sequence of the fields
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
 