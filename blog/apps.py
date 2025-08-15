from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Provides primary key type for the Blog app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
