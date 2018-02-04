#from django.http import HttpResponse, Http404
from .models import Movie
#from django.template import loader
from django.shortcuts import render, get_object_or_404

def index(request):
    #return HttpResponse("Hello, world. You're at the movies project.")
    latest_movie_list=Movie.objects.order_by('-pub_date')[:10]
    #output = ', '.join([m.movie_name for m in latest_movie_list])
    #return HttpResponse(output)
    #template = loader.get_template('movies/index.html')
    context = {
        'latest_movie_list':latest_movie_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'movies/index.html', context)

def movie_detail(request, movie_id):
    #return HttpResponse("You're looking at movie %s"%movie_id)
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404("Movie does not exist")
    # return render(request, 'movies/detail.html', {'movie':movie})
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})
