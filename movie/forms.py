from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Field
from category.models import Category
from .models import Movie


class MovieForm(forms.ModelForm):
    def __init__(self, library, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.form_type = 'edit'
            ibox_title = 'Editar filme: ' + self.instance.title
        else:
            self.form_type = 'new'
            ibox_title = 'Cadastrar novo filme'

        self.fields['category'].queryset = Category.objects.filter(library=library)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Div(
                Div(Div(
                    HTML('<h2 class="hfc-green">' + ibox_title + '</h2>'),
                    css_class='col-md-12 center'), css_class='row'),
                Div(Div(
                    Field('title'),
                    css_class='col-md-12'), css_class='row'),
                Div(Div(
                    Field('category'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('note'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('date'),
                    css_class='col-md-12'), css_class='row'),

                Div(Div(
                    Field('about'),
                    css_class='col-md-12'), css_class='row'),

                Div(
                    Submit('submit', 'Salvar', css_class="btn btn-info btn-lg"),
                    HTML('<a href="{% url "dashboard" %}" class="btn btn-outline-secondary btn-lg">Voltar</a>'),
                    css_class='row btn-group col-md-12 d-flex justify-content-end'),
                css_class='col-md-12'), css_class='row')
        )

    class Meta:
        model = Movie
        fields = ('title', 'category', 'note', 'about', 'date')

    def clean(self):
        cleaned_data = super(MovieForm, self).clean()
        date = cleaned_data.get("date")
        note = cleaned_data.get("note")

        if not date or not note:
            raise forms.ValidationError('Todos os campos devem ser preenchidos')

        if 0 <= note <= 5:
            pass
        else:
            raise forms.ValidationError({'rating': ['Nota deve ser de 0 a 5']})
