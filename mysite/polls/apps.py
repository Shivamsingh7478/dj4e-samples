from django.apps import AppConfig
import os


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
    path = os.path.dirname(os.path.abspath(__file__)) 