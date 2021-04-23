from django.apps import AppConfig


class AbstractModelAppeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abstract_model_appe'
