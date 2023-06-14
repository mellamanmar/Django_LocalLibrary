from django.views import generic
from ..models.genre import Genre

class GenreListView (generic.ListView):
    model= Genre
    context_object_name= 'genre_list'
    template_name= 'genre/genre_list.html'