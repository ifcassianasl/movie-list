from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required()
def create_movie(request):
    uuid = request.GET.get('movie_uuid')
    if uuid:
        movie = get_object_or_404(Movie, uuid=uuid)
        title = 'Editar filme: ' + movie.title
    else:
        movie = None
        title = 'Criar filme'

    form = MovieForm(request.POST or None, instance=movie)

    if form.is_valid():
        name = form.cleaned_data['title'] 
        print(name)
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
    movies = Movie.objects.filter(category__library__users__username=request.user)
    content = {
        'title': 'Meus filme',
        'movies': movies
    }

    return render(request, 'movies.html', content)


@login_required()
def delete_movie(request):
    uuid = request.GET.get('movie_uuid')
    if uuid:
        movie = get_object_or_404(Movie, uuid=uuid)
        movie.delete()
    
    return redirect('movies')