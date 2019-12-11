from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required()
def dashboard(request):
    content = {
        'title': 'Dashboard',
        'user': request.user,
    }
    return render(request, 'dashboard.html', content)

@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')
