from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email',)


class ProfileForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email',)


