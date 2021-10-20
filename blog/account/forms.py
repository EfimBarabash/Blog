from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']



class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user', 'following')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# class SubscribeForm(forms.Form):
#     subscribe = forms.CharField(widget=forms.HiddenInput, va)
#
#     def __init__(self, follow):