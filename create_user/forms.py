from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from crispy_forms.layout import Submit, Layout, Div, HTML, Field


class NewUserForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Div(
                Div(Div(
                    HTML('<h2 class="hfc-green">Cadastrar novo usuário</h2>'),
                    css_class='col-md-12 text-center'), css_class='row'),
                Div(Div(
                    Field('username'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('first_name'),
                    css_class='col-md-12'), css_class='row'),
                Div(Div(
                    Field('last_name'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('email'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('user'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('password'),
                    css_class='col-md-12'), css_class='row'),

                Div(
                    Submit('submit', 'Salvar', css_class="btn btn-primary block full-width m-b"),
                    HTML('<p class="text-muted text-center"><small>Já tem uma conta?</small></p>'
                         '<a class="btn btn-sm btn-info btn-block" href="{% url "login" %}">Login</a>'),),
                css_class='col-md-12'), css_class='row mt-5')
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    password = forms.CharField(label='Senha', widget=forms.PasswordInput())

    def check(self):
        user = self.cleaned_data['username']
        user_count = User.objects.filter(username=user).count()
        password = self.cleaned_data['password']

        if user_count != 0:
            raise forms.ValidationError({'username': ['Usuário já cadastrado', ]})
        if len(password) < 6:
            raise forms.ValidationError({'password': ['Senha fraca', ]})
