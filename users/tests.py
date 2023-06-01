from django.test import TestCase

# Create your tests here.
from django.urls import reverse
import pytest

# The django_user_model fixture is a built-in fixture. 
# It acts as a shortcut to accessing the User model for this project.
@pytest.fixture
# this creates a new user or object with the username and password
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

# this will test without us using the interface for login
def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True