from django import forms


class PasswordField(forms.CharField):
    widget = forms.PasswordInput


class LoginForm(forms.Form):
    email = forms.EmailField(label='Your email')
    password = PasswordField()
