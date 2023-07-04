import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_get_transactions():
    client = APIClient()
    url = reverse('transaction_list')  # substitua pelo nome da rota correta
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_transaction():
    client = APIClient()
    url = reverse('transaction_list')  # substitua pelo nome da rota correta
    payload = {
        'product_name': 'Product 1',
        'value': 10.0,
        'seller': '3'
    }
    response = client.post(url, data=payload)
    assert response.status_code == status.HTTP_201_CREATED