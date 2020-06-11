from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm


from .models import  Usuario
from .forms import OrderForm, CreateUserForm

def registerPage(request):
    form= CreateUserForm()

    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'accounts/register.html', context)


def user(request):
    #entries = Entry.objects.filter(usuario__startswith={'UserName': 'manuel'})
    #print('',entries)
    #entry_list = list(Entry.objects.all())
    #print(entry_list[0].usuario.UserName)
    #a = Usuario.objects.create(ident=2,UserName='manuel', Password='asdf',correo='asdf@gmail.com', almacenamiento_disp=20, id_H_Descargas=0, id_Publicacion=0, id_PDR=123 )
    #a.save()
    print("hello world")
    b=Usuario.objects.get(ident=1)
    #b.UserName="asdf"
    #b.save()
    b.delete()
    return HttpResponse("This url is working")