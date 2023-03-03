from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=100, unique=True)
    content = RichTextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Actualizacion')
    
    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title
    