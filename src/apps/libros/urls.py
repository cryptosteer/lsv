from django.conf.urls import url
from apps.libros import views

urlpatterns = [

    url(r'^inicio/', views.inicio, name='inicio'),
    url(r'^crear/', views.crear, name='crear'),
    url(r'^actualizar/', views.actualizar, name='actualizar'),
    url(r'^borrar/', views.borrar, name='borrar'),
]
