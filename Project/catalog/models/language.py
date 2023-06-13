from django.db import models

class Language(models.Model):
    book= models.ForeignKey('BookInstance', null= True, on_delete=models.SET_NULL)
    language= models.CharField(max_length=50, help_text='Ingrese el lenguaje, ejemplo inglés')
    
    def __str__(self):
        return self.name