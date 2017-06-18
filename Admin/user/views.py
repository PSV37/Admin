from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Movie
from django .http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'user/index.html'
    def get_queryset(self):
        return Movie.objects.all()

class Index1View(generic.DetailView):
    model = Movie
    template_name = 'user/index1.html'


class MovieCreate(CreateView):
    model = Movie
    fields = ['actor','actor_movie','genre']

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['actor','actor_movie','genre']

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('index')
