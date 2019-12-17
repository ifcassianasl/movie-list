from django import forms
from crispy_forms.helper import FormHelper
from .models import Library
from crispy_forms.layout import Submit, Layout, Div, HTML, Field


class LibraryForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(LibraryForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['title'].label = 'Título'
        #self.fields['title'].required = False

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Div(
                Div(Div(
                    Field('title'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('details'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('users', css_class='custom-select custom-select-lg'),
                    css_class='col-md-12'), css_class='row'),

                Div(
                    Submit('submit', 'Salvar', css_class="btn btn-info btn-lg"),
                    HTML('<a href="{% url "dashboard" %}" class="btn btn-outline-secondary btn-lg">Voltar</a>'),
                    css_class='row btn-group col-md-12 d-flex justify-content-end'),
                css_class='col-md-12'), css_class='row mt-5 w-100')
        )

    class Meta:
        model = Library
        fields = ('title', 'details', 'users')

    def clean(self):
        cleaned_data = super(LibraryForm, self).clean()
        user_list = cleaned_data.get("users")
        if self.user not in user_list:
            raise forms.ValidationError({'users': 'O seu próprio usuário deve estar selecionado!'})
