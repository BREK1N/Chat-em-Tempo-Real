"""
ASGI config for setup project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# src/setup/asgi.py
import os
from django.core.asgi import get_asgi_application

# Configura as settings antes de qualquer coisa
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django_asgi_app = get_asgi_application()

# Agora importamos as coisas do Channels (importar antes pode dar erro de AppRegistryNotReady)
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # Importa as rotas que definimos no passo anterior

application = ProtocolTypeRouter({
    # Requisições HTTP (Django padrão)
    "http": django_asgi_app,

    # Requisições WebSocket (Channels)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
