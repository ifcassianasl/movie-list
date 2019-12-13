from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from library.models import Library


@login_required()
def create_movie(request):
    user = request.user
    libraries = Library.objects.filter(users__username=user)
    active_library = get_object_or_404(Library, uuid=request.session['active_library'])

    uuid = request.GET.get('movie_uuid')
    if uuid:
        movie = get_object_or_404(Movie, uuid=uuid)
        title = 'Editar filme: ' + movie.title
    else:
        movie = None
        title = 'Criar filme'

    form = MovieForm(active_library, request.POST or None, instance=movie)

    if form.is_valid():
        this_form = form.save(commit=False)
        this_form.save()
        form.save_m2m()

        return redirect('movies')

    content = {
        'title': title,
        'form': form,
        'libraries': libraries,
    }

    return render(request, 'movie_form.html', content)


@login_required()
def movies_view(request):
    user = request.user
    libraries = Library.objects.filter(users__username=user)
    movies = Movie.objects.filter(category__library__users__username=user)

    if movies.count() == 0:
        title = 'Você não tem filmes registrados'
    else:
        title = 'Meus filmes'

    content = {
        'title': title,
        'movies': movies,
        'libraries': libraries,
    }

    return render(request, 'movies.html', content)


@login_required()
def delete_movie(request):
    uuid = request.GET.get('movie_uuid')
    if uuid:
        movie = get_object_or_404(Movie, uuid=uuid)
        movie.delete()
    
    return redirect('movies')