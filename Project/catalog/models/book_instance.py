import uuid # Requerida para las instancias de libros únicos
from django.db import models
from .language import Language
from django.urls import reverse


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    language= models.ManyToManyField(Language, help_text="Seleccione un idioma para este libro")
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
    
    def display_language(self):
        return ', '.join([ language.name for language in self.language.all()[:3] ]) 
    display_language.short_description = 'Language'

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('instance_detail', args=[str(self.id)])