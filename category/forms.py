from django import forms
from crispy_forms.helper import FormHelper
from .models import Category
from crispy_forms.layout import Submit, Layout, Div, HTML, Field


class CategoryForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Div(
                Div(Div(
                    Field('kind'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('library', css_class='custom-select custom-select-lg'),
                    css_class='col-md-12'), css_class='row'),

                Div(
                    Submit('submit', 'Salvar', css_class="btn btn-info btn-lg"),
                    HTML('<a href="{% url "dashboard" %}" class="btn btn-outline-secondary btn-lg">Voltar</a>'),
                    css_class='row btn-group col-md-12 d-flex justify-content-end'),
                css_class='col-md-12'), css_class='row mt-5 w-100')
        )

    class Meta:
        model = Category
        fields = ('kind', 'library')
