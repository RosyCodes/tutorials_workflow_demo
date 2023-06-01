from django.test import TestCase


# Create your tests here.
from django.urls import reverse
from tutorials.models import Tutorial
import pytest

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

#  integration tests to see whether we can successfully interact with the database via Django models/ORM.
# @pytest.mark.django_db # to address the error for db access 
# # @pytest.mark.django_db -used to allow this test access to the connected database, which is required by this particular view. 
# def test_create_tutorial():
#     tutorial = Tutorial.objects.create(
#         title='Pytest',
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#         description='Tutorial on how to apply pytest to a Django application',
#         published=True
#     )
#     assert tutorial.title == "Pytest"

# === the test above works to see if we can connect with the db


# the test belo is to write more integration tests for creating tutorial object
@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# the methods below will use the fixture above
def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

#creating another object
@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk