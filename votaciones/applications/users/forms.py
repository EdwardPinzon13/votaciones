from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username=forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder' :'username',
            'style':{'margin:10px'}
        }))
    password=forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder':'contrasena'
        })
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de inicio de sesión no son correctos')
        return self.cleaned_data