from django.urls import path
from .utils import subir_documento,lista_documentos,seleccionar_idioma,texto_simplificado,descargar_traduccion_pdf,eliminar_documento
from .views import analizar_documento,traducir_documento
urlpatterns = [
    path('subir/', subir_documento, name='subir_documento'),
    path('lista/', lista_documentos, name='lista_documentos'),
    path('inspeccionar/<int:documento_id>/', analizar_documento, name='inspeccionar_documento'),
    path('seleccionar_idioma/<int:documento_id>/', seleccionar_idioma, name='seleccionar_idioma'),
    path('traducir/<int:documento_id>/', traducir_documento, name='traducir_documento'),
    path('documento/<int:documento_id>/simplificado/', texto_simplificado, name='simplificar_texto'),
    path('descargar-traduccion-pdf/', descargar_traduccion_pdf, name='descargar_traduccion_pdf'),
    path('eliminar/<int:documento_id>/', eliminar_documento, name='eliminar_documento')

]

