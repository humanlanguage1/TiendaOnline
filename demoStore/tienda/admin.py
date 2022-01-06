from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto 

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display= ('pk','nombre','categoria','precio','stock')
    list_display_links= ('pk','nombre')
    list_ediable= ('categoria','precio','stock')
    search_fields= ('nombre')

