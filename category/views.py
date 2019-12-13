from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required()
def create_categories(request):
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
    categories = Category.objects.filter(library__users__username=request.user)
    content = {
        'title': 'Minhas categorias',
        'categories': categories
    }

    return render(request, 'categories.html', content)


@login_required()
def delete_category(request):
    uuid = request.GET.get('category_uuid')
    if uuid:
        category = get_object_or_404(Category, uuid=uuid)
        category.delete()
    
    return redirect('categories')