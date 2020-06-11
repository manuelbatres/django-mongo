from djongo import models

# Create your models here.
class Usuario(models.Model):
    _id = models.ObjectIdField(default='666f6f2d6261722d71757578')
    ident = models.IntegerField()
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    almacenamiento_disp = models.IntegerField()
    id_H_Descargas = models.IntegerField()
    id_Publicacion = models.IntegerField()
    id_PDR = models.IntegerField()
    objects = models.DjongoManager()

    

