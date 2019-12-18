from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from library.models import Library
from rest_framework import viewsets
from .serializers import CategorySerializer


@login_required()
def create_categories(request):
    library = request.session['active_library']
    active_library = get_object_or_404(Library, uuid=library)

    uuid = request.GET.get('category_uuid')
    if uuid:
        category = get_object_or_404(Category, uuid=uuid)
        title = 'Editar categoria: ' + category.kind
    else:
        category = None
        title = 'Criar categoria'

    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        this_form = form.save(commit=False)
        this_form.library = active_library
        this_form.save()
        form.save_m2m()

        return redirect('categories')

    content = {
        'title': title,
        'form': form,
    }

    return render(request, 'category_form.html', content)


@login_required()
def categories_view(request):
    if request.session['active_library']:
        library = request.session['active_library']
        categories = Category.objects.filter(library__uuid=library)
        if categories.count() == 0:
            title = "Você não tem categorias nessa lista"
        else:
            title = "Minhas categorias"
    else:
        title = "Escolha uma lista!"
        categories = []

    content = {
        'title': title,
        'categories': categories,
    }

    return render(request, 'categories.html', content)


@login_required()
def delete_category(request):
    uuid = request.GET.get('category_uuid')
    if uuid:
        category = get_object_or_404(Category, uuid=uuid)
        category.delete()
    
    return redirect('categories')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
