from django.views.generic import ListView, CreateView, UpdateView

from viewer.models import Movie
from viewer.forms import MovieForm
from django.urls import reverse_lazy
from logging import getLogger
LOGGER = getLogger()

class MoviesView(ListView):
   template_name = 'movies.html'
   model = Movie

class MovieCreateView(CreateView):
   template_name = 'form.html'
   form_class =  MovieForm
   success_url = reverse_lazy('movie_create')


   def form_invalid(self, form):
      LOGGER.warning('User provided invalid data')
      return super().form_invalid(form)


class MovieUpdateView(UpdateView):
   template_name = 'form.html'
   form_class = MovieForm
   success_url = reverse_lazy('index')
   model = Movie

   def form_invalid(self, form):
      LOGGER.warning('User provided invalid data')
      return super().form_invalid(form)



