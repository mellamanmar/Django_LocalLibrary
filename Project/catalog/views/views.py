from django.shortcuts import render

# Create your views here.

from ..models.author import Author
from ..models.genre import  Genre

def index(request):
    """Function to home site"""
    authors= Author.objects.all()
    genres= Genre.objects.all()

    return render(
        request,
        'index.html',
        context=
        {
            "authors":authors,
            "genres":genres
        }
    )