import pytest
from apps.models import *
from rest_framework.test import APIClient


class TestCategory:
    @pytest.fixture
    def api_client(self):
        category = Category.objects.create(name='Sport')
        Book.objects.create(title="Book", author="Author1", page=100, description="...", amount=10,
                            category_id=category.id, money_type="USD")

        return APIClient()

    @pytest.mark.django_db
    def test_category_create(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/create'
        response = api_client.post(url, data={'name': 'History'})
        assert response.status_code == 201
        created = Category.objects.get(name='Sport')
        assert created is not None

    @pytest.mark.django_db
    def test_category_get(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/get'
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_category_get(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/get'
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_category_search(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/search?category_id=4'
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_category_update(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/update7'
        response = api_client.patch(url)
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_category_delete(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/delete1'
        response = api_client.delete(url)
        assert response.status_code == 204
        assert Category.objects.count() == 0

    @pytest.mark.django_db
    def test_category_delete(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/book/list'
        response = api_client.get(url)
        assert response.status_code == 200
        assert Book.objects.count() == 1

    # ========================================================  BOOK TEST  ========================================
    @pytest.mark.django_db
    def test_book_create(self, api_client: APIClient):
        category = Category.objects.create(name='Sport')
        url = 'http://localhost:8000/api/v1/book/create'
        response = api_client.post(url, data={
            'title': "Book",
            'author': "Author1",
            'page': 100,
            'description': "...",
            'amount': 10,
            'category_id': category.id,
            'money_type': "USD",
        })
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_book_create(self, api_client: APIClient):
        # category = Category.objects.create(name='Sport')
        url = 'http://127.0.0.1:8000/api/v1/id/book?book_id=1'
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_book_update_patch(self, api_client: APIClient):
        url = 'http://127.0.0.1:8000/api/v1/id/book?book_id=1'
        response = api_client.get(url)
        assert response.status_code == 200
        url = 'http://127.0.0.1:8000/api/v1/update/book1'
        assert Book.objects.count() == 1
        response = api_client.patch(url)
        assert response.status_code == 200
