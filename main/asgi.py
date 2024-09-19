"""
ASGI config for application_data_mgt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from main.utils.env_loader import default_env
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', default_env.DJANGO_SETTINGS_MODULE)

application = get_asgi_application()
