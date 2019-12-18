from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import EditUserForm
from rest_framework import viewsets
from .serializers import UserSerializer


@login_required()
def account(request):
    content = {
        'title': 'Minha conta',
        'user': get_object_or_404(User, username=request.user),
    }
    return render(request, 'user.html', content)


@login_required()
def edit_account(request):
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
    }
    return render(request, 'edit_user.html', content)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
