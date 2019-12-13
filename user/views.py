from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import EditUserForm
from library.models import Library


@login_required()
def account(request):
    user = request.user
    libraries = Library.objects.filter(users__username=user)

    content = {
        'title': 'Minha conta',
        'user': get_object_or_404(User, username=user),
        'libraries':libraries,
    }
    return render(request, 'user.html', content)


@login_required()
def edit_account(request):
    user = request.user
    libraries = Library.objects.filter(users__username=user)

    user = get_object_or_404(User, username=request.user)
    form = EditUserForm(request.POST or None, instance=user)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password)
        user.save()
        return redirect('/')

    content = {
        'title': 'Editar conta',
        'user': user,
        'form': form,
        'libraries': libraries,
    }
    return render(request, 'edit_user.html', content)
