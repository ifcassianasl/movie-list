from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from crispy_forms.layout import Submit, Layout, Div, HTML, Field


class NewUserForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.form_type = 'edit'
            ibox_title = 'Editar filme: ' + self.instance.title
        else:
            self.form_type = 'new'
            ibox_title = 'Cadastrar novo usuário'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Div(
                Div(Div(
                    HTML('<h2 class="hfc-green">' + ibox_title + '</h2>'),
                    css_class='col-md-12 text-center'), css_class='row'),
                Div(Div(
                    Field('username'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('first_name'),
                    css_class='col-md-6'),
                    Div(
                    Field('last_name'),
                    css_class='col-md-6'), css_class='row'),

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
                    Submit('submit', 'Salvar', css_class="btn btn-success btn-lg"),
                    HTML('<a href="#" class="btn btn-outline-secondary btn-lg">Voltar</a>'),
                    css_class='row btn-group col-md-12 d-flex justify-content-end'),
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
