from django.urls import include, path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista, name='lista'),
    path('detalhe/', views.detalhe, name='detalhe'),
]

# rotas: Home, Lista e Detalhe.