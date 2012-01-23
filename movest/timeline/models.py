from django.db import models

TIPOS = (
    ('Noticia', 'Noticia'),
    ('Documento Oficial', 'Documento Oficial'),
    ('Comentario', 'Comentario o Tweet'),
    ('Entrevista', 'Entrevista'),
    ('Columna o Blog Post', 'Columna o Blog Post'),
    ('Solo Video', 'Solo Video'),
    ('Solo Audio', 'Solo Audio'),
    ('Foto o Imagen', 'Foto o Imagen')
)

FORMATOS = (
    ('Texto', 'Texto'),
    ('Imagen', 'Imagen'),
    ('Audio', 'Audio'),
    ('Video', 'Video'),
    ('Multimedia', 'Multimedia')
)

# Create your models here.

class Fecha(models.Model):
    fecha = models.DateField('fecha del suceso', unique=True)
    
    def __unicode__(self):
        return str(self.fecha)
    
class Autor(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=144)
    url = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Autores"
    
class Lugar(models.Model):
    pais = models.CharField(max_length=32, null=True)
    region = models.CharField(max_length=32, null=True)
    ciudad = models.CharField(max_length=32, null=True)
    direccion = models.CharField(max_length=64, null=True)
    coordenadas = models.CharField(max_length=64, null=True)
    
    class Meta:
        verbose_name_plural = "Lugares"
    
class Tipo(models.Model):
    tipo = models.CharField(max_length=20, choices=TIPOS, unique=True)
    
    def __unicode__(self):
        return self.tipo

class Formato(models.Model):
    formato = models.CharField(max_length=10, choices=FORMATOS, unique=True)
    
    def __unicode__(self):
        return self.formato
    
class Fuente(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    url = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.nombre
    
class Evento(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=512)
    fecha_publicacion = models.DateTimeField('fecha de publicacion')
    fecha_suceso = models.ForeignKey(Fecha)
    lugar = models.ForeignKey(Lugar)
    
    def __unicode__(self):
        return self.nombre
    
class Recurso(models.Model):
    titulo = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    status = models.IntegerField(null=True)
    fecha_publicacion = models.DateTimeField('fecha de publicacion')
    fecha_suceso = models.ForeignKey(Fecha)
    autor = models.ForeignKey(Autor, null=True)
    tipo = models.ForeignKey(Tipo, null=True)
    formato = models.ForeignKey(Formato, null=True)
    lugar = models.ForeignKey(Lugar, null=True)
    evento = models.ForeignKey(Evento, null=True)
    fuente = models.ForeignKey(Fuente, null=True)

    def __unicode__(self):
        return self.url

    

    
