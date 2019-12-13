from django.shortcuts import render, redirect
from .forms import LibraryForm
from .models import Library
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required()
def create_library(request):
    uuid = request.GET.get('library_uuid')
    if uuid:
        library = get_object_or_404(Library, uuid=uuid)
        title = 'Editar lista: ' + library.title
    else:
        library = None
        title = 'Criar lista'

    form = LibraryForm(request.POST or None, instance=library)

    if form.is_valid():
        this_form = form.save(commit=False)
        this_form.save()
        form.save_m2m()

        return redirect('libraries')

    content = {
        'title': title,
        'form': form,
    }

    return render(request, 'library_form.html', content)


@login_required()
def libraries_view(request):
    user = request.user
    libraries = Library.objects.filter(users__username=user)
    content = {
        'title': 'Minhas listas',
        'user': user,
        'libraries': libraries
    }

    return render(request, 'libraries.html', content)


@login_required()
def delete_library(request):
    uuid = request.GET.get('library_uuid')
    if uuid:
        library = get_object_or_404(Library, uuid=uuid)
        library.delete()
    
    return redirect('libraries')