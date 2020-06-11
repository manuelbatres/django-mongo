from djongo import models

# Create your models here.
class Usuario(models.Model):
    ident = models.IntegerField()
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    almacenamiento_disp = models.IntegerField()
    id_H_Descargas = models.IntegerField()
    id_Publicacion = models.IntegerField()
    id_PDR = models.IntegerField()

    class Meta:
        abstract = True
    
class Entry(models.Model):
    _id = models.ObjectIdField()
    usuario = models.EmbeddedField(
        model_container=Usuario,
    )
    headline = models.CharField(max_length=255)    
    objects = models.DjongoManager()