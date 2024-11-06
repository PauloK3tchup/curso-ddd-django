import pytest
from rest_framework import status
from rest_framework.test import APIClient
from core.publisher.domain.entities import Publisher
from core.publisher.infra.publisher_django_app.repository import DjangoORMPublisherRepository

@pytest.mark.django_db

@pytest.fixture
def a_publisher() -> Publisher:
    return Publisher(
        name='Test Publisher',
        description='Test Description',
    )

@pytest.fixture
def publisher_repository():
    return DjangoORMPublisherRepository()

class TestCreatePublisherView:
    def test_list_publisher(
            self,
            publisher_repository: DjangoORMPublisherRepository,
            a_publisher: Publisher
        ):
        
        publisher_repository.create(a_publisher)
        url = '/api/publishers/'
        response = APIClient().get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['id'] == a_publisher.id
        assert response.data[0]['name'] == a_publisher.name
        assert response.data[0]['description'] == a_publisher.description
        assert response.data[0]['is_active'] == a_publisher.is_active
