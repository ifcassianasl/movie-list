from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from library.models import Library
from .serializers import MovieSerializer
from rest_framework import viewsets


@login_required()
def create_movie(request):
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
    }

    return render(request, 'movie_form.html', content)


@login_required()
def movies_view(request):
    if request.session['active_library']:
        library = request.session['active_library']
        movies = Movie.objects.filter(category__library__uuid=library)

        if movies.count() == 0:
            title = 'Você não tem filmes registrados'
        else:
            title = 'Meus filmes'
    else:
        title = "Escolha uma lista!"
        movies = []

    content = {
        'title': title,
        'movies': movies,
    }

    return render(request, 'movies.html', content)


@login_required()
def delete_movie(request):
    uuid = request.GET.get('movie_uuid')
    if uuid:
        movie = get_object_or_404(Movie, uuid=uuid)
        movie.delete()
    
    return redirect('movies')


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
