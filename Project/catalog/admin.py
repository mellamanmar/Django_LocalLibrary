from django.contrib import admin

# Register your models here.

from .models.author import Author
from .models.genre import Genre
from .models.book import Book
from .models.book_instance import BookInstance
from .models.language import Language

class AuthorInstanceInline(admin.TabularInline):
    model = Book
    extra= 0
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorInstanceInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register (Language)
admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
        model = BookInstance
        extra= 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ["book", "status", "due_back", "id", "display_language"]
    list_filter = ('status', 'due_back')
    fieldsets = (
        (Book.title, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    


