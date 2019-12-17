from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required()
def dashboard(request):
    user = request.user

    content = {
        'title': 'Dashboard',
        'user': user,
    }
    return render(request, 'dashboard/index.html', content)


@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')
