import pytest
import os
import sys
from django.conf import settings
from blog.factories import PostFactory

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mysite'))

if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    settings.configure()

import django
django.setup()

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
