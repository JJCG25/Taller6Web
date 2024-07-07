from django.urls import path
from . import views

urlpatterns = [
    path('',views.tiposd,name='tiposd'),
    path('nuevo/', views.create_tiposd, name='crear_tipodocumento'),
    path('editar/<int:pk>/', views.edit_tiposd, name='editar_tipodocumento'),
    path('eliminar/<int:pk>/', views.delete_tiposd, name='delete_tipodocumento'),
]