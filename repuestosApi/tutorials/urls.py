from django.urls import re_path
from tutorials.cliente.view import cliente_list, cliente_detail
from tutorials.modelo.view import modelo_list
from tutorials.repuesto.view import repuesto_modelos, repuesto_modelos_detail
from tutorials.repuesto.view import repuesto_list, repuesto_detail
from tutorials.genero.view import genero_list

urlpatterns = [
    re_path(r'^api/cliente$', cliente_list )
    , re_path(r'^api/cliente/(?P<id>\d+)$', cliente_detail )
    , re_path(r'^api/modelos$', modelo_list )
      , re_path(r'^api/repuestos$', repuesto_list )
    , re_path(r'^api/repuestos/(?P<id>\d+)$', repuesto_detail )
    , re_path(r'^api/repuestos/(?P<id>\d+)/modelos$', repuesto_modelos )
    , re_path(r'^api/repuestos/(?P<id>\d+)/modelos/(?P<id_modelo>\d+)$', repuesto_modelos_detail )

    , re_path(r'^api/generos$', genero_list )
]