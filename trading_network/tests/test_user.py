import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from user.models import User


@pytest.mark.django_db
def test_user_registration():
    url = reverse('user:register')
    data = {
        "email": "user@gmail.com",
        "password": "qwertyui"
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert User.objects.count() == 1
