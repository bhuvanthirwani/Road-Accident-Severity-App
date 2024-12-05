"""
WSGI config for road_accident_severity_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.getenv('POETRY_VIRTUAL_ENV'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'road_accident_severity_app.settings')

application = get_wsgi_application()
