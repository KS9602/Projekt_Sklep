from django.apps import AppConfig


class SuperShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'super_shop'
    
    def ready(self):
        import super_shop.signals
