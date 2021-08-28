from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from viewer.models import Movie

def movies(request):
    s = request.GET.get('s', '')
    return render(
        request, template_name='movies.html',
        context={
            'movies': Movie.objects.all()

        }

    )