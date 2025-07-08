from django.apps import AppConfig


class AerolineaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aerolinea'

    def ready(self):
        """
        Metodo que se ejecuta cuando la app esta lista y 
        se importan los signals evitando los problemas de 
        """
        from aerolinea import signals
        return super().ready()