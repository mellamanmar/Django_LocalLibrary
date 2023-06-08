from django.contrib import admin

# Register your models here.

from .models.author import Author
from .models.genre import Genre
from .models.book import Book
from .models.book_instance import BookInstance
from .models.language import Language

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register (Book) 
admin.site.register (Language)