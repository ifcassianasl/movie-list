from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from crispy_forms.layout import Submit, Layout, Div, HTML, Field


class EditUserForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Div(
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
                    Submit('submit', 'Salvar', css_class="btn btn-info btn-lg"),
                    HTML('<a href="{% url "dashboard" %}" class="btn btn-outline-secondary btn-lg">Voltar</a>'),
                    css_class='row btn-group col-md-12 d-flex justify-content-end'),
                css_class='col-md-12'), css_class='row mt-5 w-100'),
        )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    password = forms.CharField(label='Nova senha', widget=forms.PasswordInput())

    def check(self):
        password = self.cleaned_data['password']

        if len(password) < 6:
            raise forms.ValidationError({'password': ['Senha fraca', ]})
