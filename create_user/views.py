from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib.auth.models import User


def user_view(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email,
                                   is_staff=1, is_superuser=1)
        user.set_password(password)
        user.save()

        user_auth = authenticate(username=username, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect('/dashboard/')

    content = {
        'title': 'Criar conta:',
        'form': form,
    }

    return render(request, 'index.html', content)
