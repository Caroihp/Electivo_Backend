from django.contrib import admin
from tienda.models import Producto, Categoria

admin.site.site_header ='Administracion de la tienda'
admin.site.site_title='Tienda Admin'
admin.site.index_title='Panel de Administracion de la tienda'

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','categoria')
    #search_fields=('nombre','categoria__nombre')
    search_fields=('nombre',)
    list_filter=('categoria',)
    #list_editable=('precio',)
    list_per_page=20
    ordering=('precio',)
    fields=('nombre','precio','stock','categoria')
    #fieldsets=()

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)