from django.conf.urls import url

from apps.materias import views

urlpatterns = [
    url(r'^crear', views.crear, name='crear'),
    url(r'^borrar', views.borrar, name='borrar'),
    url(r'^editar', views.editar, name='editar'),
    url(r'^notas', views.notas, name='notas'),
    url(r'^inicio', views.inicio, name='inicio'),
]