
from django.urls import path
from aerolinea.views import (

    AvionCreateView,
    AvionDelete,
    AvionDetail,
    AvionList,    

    BoletoList,
    BoletoCreate,

    VueloCreate,
    VueloList,
    VueloDetail,
    VueloCreate,
    VueloDelete,

    PasajeroCreate,
    PasajeroList,
    PasajerosVueloListView,
    HistorialPasajeroView,

    ReservaCreate,
    ReservaList,
    ReservaDelete,

    AsientoCreate,
    AsientoList,
)

urlpatterns = [
    path(
        route="avion_list/", 
        view=AvionList.as_view(), 
        name="avion_list"
    ),
    path(
        route="avion_detail/<int:avion_id>/",
        view=AvionDetail.as_view(),
        name="avion_detail",
    ),
    path(
        route="avion_delete/<int:avion_id>/",
        view=AvionDelete.as_view(),
        name="avion_delete",
    ),
    path(
        route="avion_create/", 
        view=AvionCreateView.as_view(), 
        name="avion_create"
    ),
    
    path(
        route="vuelo_create/", 
        view=VueloCreate.as_view(), 
        name="vuelo_create"
    ),    
    path(
        route="vuelo_list/", 
        view=VueloList.as_view(), 
        name="vuelo_list"
    ),    
    path(
        route="vuelo_detail//<int:vuelo_id>/", 
        view=VueloDetail.as_view(), 
        name="vuelo_detail"
    ),
    path(
        route="vuelo_delete/<int:vuelo_id>/", 
        view=VueloDelete.as_view(), 
        name="vuelo_delete"
    ),    
    path(
        route="vuelo/<int:vuelo_id>/pasajeros",
        view=PasajerosVueloListView.as_view(),
        name="vuelo_pasajeros"
    ),


    path(
        route="boleto_list/", 
        view=BoletoList.as_view(), 
        name="boleto_list"
    ),
    path(
        route="boleto_create/", 
        view=BoletoCreate.as_view(), 
        name="boleto_create"
    ),    

    path(
        route="pasajero_create/", 
        view=PasajeroCreate.as_view(), 
        name="pasajero_create"
    ),    
    path(
        route="pasajero_list/", 
        view=PasajeroList.as_view(), 
        name="pasajero_list"
    ),        
    path(
        route="pasajero/<int:pasajero_id>/historial", 
        view=HistorialPasajeroView.as_view(), 
        name="pasajero_historial"
    ),

    path(
        route="reserva_create/", 
        view=ReservaCreate.as_view(), 
        name="reserva_create"
    ),    
    path(
        route="reserva_list/", 
        view=ReservaList.as_view(), 
        name="reserva_list"
    ),
    path(
        route="reserva_delete/<int:reserva_id>/", 
        view=ReservaDelete.as_view(), 
        name="reserva_delete"
    ),    

    path(
        route="asiento_create/", 
        view=AsientoCreate.as_view(), 
        name="asiento_create"
    ),    
    path(
        route="asiento_list/", 
        view=AsientoList.as_view(), 
        name="asiento_list"
    ),
]
