from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@login_required()
def account(request):
    content = {
        'title': 'Minha conta',
        'user': get_object_or_404(User, username=request.user),
    }
    return render(request, 'user.html', content)
