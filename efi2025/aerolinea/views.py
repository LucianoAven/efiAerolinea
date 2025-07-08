from aerolinea.models import Asiento, Avion, Boleto, Pasajero, Reserva, Vuelo
from aerolinea.models import HistoricalReserva

# Vistas inspiradas en clases
from django.views.generic import (
    DetailView, 
    DeleteView,
    ListView,
    CreateView
)
from django.urls import reverse_lazy

# Importacion de formularios para cada entidad
from aerolinea.forms import (
    VueloForm,
    PasajeroForm,
    ReservaForm,
    AsientoForm,
    BoletoForm,
)

# Para historial de reservas
HistoricalReserva = Reserva.history.model

# Vistas CRUD para los modelos
class AvionList(ListView):
    model = Avion 
    template_name = 'avion/list.html'
    context_object_name = 'aviones'


class AvionDetail(DetailView):
    model = Avion
    template_name = 'avion/detail.html'
    context_object_name = 'avion'
    pk_url_kwarg = 'avion_id' # Nombre con el que buscara el id en la ruta


class AvionDelete(DeleteView):
    model = Avion
    template_name = 'avion/delete.html'
    pk_url_kwarg = 'avion_id'
    success_url = reverse_lazy('avion_list')


class AvionCreateView(CreateView):
    model = Avion
    template_name = 'avion/create.html'
    success_url = reverse_lazy('avion_list')
    fields = ['modelo', 'capacidad', 'filas', 'columnas']


class VueloList(ListView):
    model = Vuelo
    template_name = 'vuelo/list.html'
    context_object_name = 'vuelos'


class VueloDetail(DetailView):
    model = Vuelo
    template_name = 'vuelo/detail.html'
    context_object_name = 'vuelo'
    pk_url_kwarg = 'vuelo_id'


class VueloCreate(CreateView):
    model = Vuelo
    form_class = VueloForm
    template_name = 'vuelo/create.html'
    success_url = reverse_lazy('vuelo_create')


class VueloDelete(DeleteView):
    model = Vuelo
    template_name = 'vuelo/delete.html'
    pk_url_kwarg = 'vuelo_id'
    success_url = reverse_lazy('vuelo_list')


class BoletoList(ListView):
    model = Boleto 
    template_name = 'boleto/list.html'
    context_object_name = 'boletos'


class BoletoCreate(CreateView):
    model = Boleto
    form_class = BoletoForm
    template_name = 'boleto/create.html'
    success_url = reverse_lazy('boleto_create')


class PasajeroList(ListView):
    model = Pasajero 
    template_name = 'pasajero/list.html'
    context_object_name = 'pasajeros'


class PasajeroCreate(CreateView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = 'pasajero/create.html'
    success_url = reverse_lazy('pasajero_create')


class PasajerosVueloListView(ListView):

    # Lista de pasajeros asociados a un vuelo especifico

    model = Pasajero
    template_name = 'vuelo/pasajeros.html'
    context_object_name = 'pasajeros'

    def get_queryset(self):
        vuelo_id = self.kwargs.get('vuelo_id')
        return Pasajero.objects.filter(
            reserva__vuelo_id=vuelo_id
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vuelo_id = self.kwargs.get('vuelo_id')
        context['vuelo'] = Vuelo.objects.get(pk=vuelo_id)
        return context


class HistorialPasajeroView(DetailView):

    # Detalle de pasajero y su historial de reserva

    model = Pasajero
    template_name = 'pasajero/historial.html'
    context_object_name = 'pasajero'
    pk_url_kwarg = 'pasajero_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pasajero = self.get_object()

        # Consultar directamente el historial de reservas, filtrando por pasajero
        historial_reservas = (
            HistoricalReserva.objects
            .filter(pasajero_id=pasajero.id)
            .order_by('-history_date')
        )

        context['historial_reservas'] = historial_reservas
        return context


class ReservaList(ListView):
    model = Reserva 
    template_name = 'reserva/list.html'
    context_object_name = 'reservas'


class ReservaCreate(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reserva/create.html'
    success_url = reverse_lazy('reserva_create')


class ReservaDelete(DeleteView):
    model = Reserva
    template_name = 'reserva/delete.html'
    pk_url_kwarg = 'reserva_id'
    success_url = reverse_lazy('reserva_list')


class AsientoList(ListView):
    model = Asiento 
    template_name = 'asiento/list.html'
    context_object_name = 'asientos'


class AsientoCreate(CreateView):
    model = Asiento
    form_class = AsientoForm
    template_name = 'asiento/create.html'
    success_url = reverse_lazy('asiento_create')

