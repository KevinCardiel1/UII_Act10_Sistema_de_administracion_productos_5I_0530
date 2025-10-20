from django.apps import AppConfig


class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_productos'
    # Keep the original app label so existing migrations and DB tables
    # that reference 'productos' continue to work.
    label = 'productos'
