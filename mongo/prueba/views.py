from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import  Usuario

def user(request):
    #entries = Entry.objects.filter(usuario__startswith={'UserName': 'manuel'})
    #print('',entries)
    #entry_list = list(Entry.objects.all())
    #print(entry_list[0].usuario.UserName)
    a = Usuario(ident=1,UserName='manuel', Password='asdf',correo='asdf@gmail.com', almacenamiento_disp=20, id_H_Descargas=0, id_Publicacion=0, id_PDR=123 )
    a.save()
    print("hello world")

    return HttpResponse("This url is working")