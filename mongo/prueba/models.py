from djongo import models

# Create your models here.
class Usuario(models.Model):
    _id = models.ObjectIdField()
    ident = models.IntegerField()
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    almacenamiento_disp = models.IntegerField()
    id_H_Descargas = models.IntegerField()
    id_Publicacion = models.IntegerField()
    id_PDR = models.IntegerField()
    objects = models.DjongoManager()

    
class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

