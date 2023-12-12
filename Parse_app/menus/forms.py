from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

class UserLoginForm(AuthenticationForm):
    pass

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid Email Address please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user