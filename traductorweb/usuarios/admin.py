# Register your models here.
from django.contrib import admin
from .models import Usuario  # Importar el modelo de usuario personalizado

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')  # Campos visibles en la lista
    search_fields = ('username', 'email')  # Permite buscar usuarios por nombre o email
    list_filter = ('is_active', 'is_staff', 'is_superuser')  # Filtros en la interfaz
    ordering = ('id',)  # Ordena los usuarios por ID
