import os
import sys
from django.conf import settings

# Adicione o diretório 'mysite' ao sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mysite'))

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
settings.configure()

# Inicialização do Django
import django
django.setup()