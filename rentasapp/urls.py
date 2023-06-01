from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('signup/', views.signup, name='signup'),
        path('anuncio/', views.anuncio, name='anuncio'),
        path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
        path('login/', views.inicio_sesion, name='iniciar_sesion'),
        path('anuncio/create/', views.crear_anuncio, name='crear_anuncio')
]