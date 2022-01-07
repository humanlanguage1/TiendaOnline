from django.shortcuts import render
from django.conf import settings
from .models import Producto


def index(request):
    lista_productos = Producto.objects.all()
    print(settings.MEDIA_URL)
    context = {'lstProductos' :lista_productos,'directorio_img':settings.MEDIA_URL}
    return render(request,'index.html',context)

def registro(request):
    return render(request,'registroCliente.html')
