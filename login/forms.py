from django import forms
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, HTML


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())

    def __init__(self,  *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Div(
                Div(Div(
                    HTML('<h2>Acessar conta</h2>'),
                    css_class='col-md-12 text-center mb-5'), css_class='row'),
                Div(Div(
                    Field('username'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('password'),
                    css_class='col-md-12'), css_class='row'),

                Div(
                    Submit('submit', 'Entrar', css_class="btn btn-success btn-lg"),
                    css_class='row col-md-12 d-flex justify-content-end'),
                css_class='col-md-12'), css_class='row mt-5')
        )

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Login inválido')
