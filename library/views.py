from django.shortcuts import render, redirect
from .forms import LibraryForm
from .models import Library


def create_library(request):
    form = LibraryForm(request.POST or None)

    if form.is_valid():
        title = form.cleaned_data['title']
        details = form.cleaned_data['details']
        users = form.cleaned_data['users']

        library = Library.objects.create(title=title, details=details)
        library.users.set(users)
        library.save()

        return redirect('libraries')

    content = {
        'title': 'Criar lista',
        'form': form,
    }

    return render(request, 'library_form.html', content)


def libraries_view(request):
    user = request.user
    libraries = Library.objects.filter(users__username=user)
    content = {
        'title': 'Minhas listas',
        'user': user,
        'libraries': libraries
    }

    return render(request, 'libraries.html', content)
