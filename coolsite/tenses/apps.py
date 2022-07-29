from django.apps import AppConfig


class TensesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenses'
    verbose_name = 'Времена'


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category'
    verbose_name = 'Категория'
