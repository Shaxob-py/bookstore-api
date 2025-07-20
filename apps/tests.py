import pytest
from django.contrib.auth.models import User

from apps.models import *
from rest_framework.test import APIClient


class TestCategory:
    @pytest.fixture
    def api_client(self):
        Category.objects.create(name="Book")
        Category.objects.create(name="Texnika")
        Category.objects.create(name="Home")

        user = User.objects.create(username="admin")
        user.set_password("1")
        user.save()
        return APIClient()

    @pytest.mark.django_db
    def test_book_list_with_data(api_client: APIClient):
        Book.objects.create(title="Book 1", amount=5, money_type="USD")
        Book.objects.create(title="Book 2", amount=10, money_type="UZS")

        url = 'http://localhost:8000/api/v1/book/list'
        response = api_client.get(url)

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]['title'] == "Book 1"

    @pytest.mark.django_db
    def test_book_create(self, api_client):
        url = 'http://localhost:8000/api/v1/book/create'

        payload = {
            "title": "New Book",
            "amount": 3,
            "money_type": "USD"
        }

        response = api_client.post(url, data=payload, format='json')

        assert response.status_code == 201
        assert Book.objects.filter(title="New Book").exists()

    @pytest.mark.django_db
    def test_book_get_list_api_view(api_client):
        book1 = Book.objects.create(title="Book 1", amount=5, money_type="USD")
        book2 = Book.objects.create(title="Book 2", amount=3, money_type="UZS")

        url = 'http://localhost:8000/api/v1/book/id/book'

        response_all = api_client.get(url)
        assert response_all.status_code == 200
        data_all = response_all.json()
        assert isinstance(data_all, list)
        assert len(data_all) == 2

        response_one = api_client.get(url, {'book_id': book1.id})
        assert response_one.status_code == 200
        data_one = response_one.json()
        assert len(data_one) == 1
        assert data_one[0]['title'] == "Book 1"

    @pytest.mark.django_db
    def test_book_update_api_view(api_client):
        book = Book.objects.create(title="Old Title", amount=5, money_type="USD")

        url = f'http://localhost:8000/api/v1/book/update/{book.pk}'

        payload = {
            "title": "Updated Title",
            "amount": 10,
            "money_type": "UZS"
        }

        response = api_client.patch(url, data=payload, format='json')
        assert response.status_code in (200, 202)

        updated_book = Book.objects.get(id=book.id)
        assert updated_book.title == "Updated Title"
        assert updated_book.amount == 10
        assert updated_book.money_type == "UZS"

    @pytest.mark.django_db
    def test_book_delete_api_view(api_client):
        book = Book.objects.create(title="Test Book", amount=5, money_type="USD")

        url = f'http://localhost:8000/api/v1/book/delete/{book.id}'

        response = api_client.delete(url)
        assert response.status_code in (200, 204)

        exists = Book.objects.filter(id=book.id).exists()
        assert not exists

    # @pytest.mark.django_db
    # def test_category_list(self, api_client: APIClient):
    #     url = 'http://localhost:8000/api/v1/category/list'
    #     response = api_client.get(url)
    #     assert response.status_code == 200
    #     assert len(response.json()) == 3
    #
    #
    # @pytest.mark.django_db
    # def test_category_delete(self, api_client: APIClient):
    #     login_url = 'http://localhost:8000/api/v1/login'
    #     response = api_client.post(login_url , data={"username": "admin" , "password":1})
    #     assert response.status_code == 200
    #     assert "access" in response.json().keys()
    #     access_token = response.json().get('access')
    #
    #
    #     url = 'http://localhost:8000/api/v1/category/delete/2'
    #     response = api_client.delete(url , headers={"Authorization" : f"Bearer {access_token}"})
    #     assert response.status_code == 204
    #     url = 'http://localhost:8000/api/v1/category/list'
    #     response = api_client.get(url)
    #     assert response.status_code == 200
    #     assert len(response.json()) == 2
    #     obj = DeleteCategory.objects.filter(category_id=2)
    #     assert obj.exists() and obj.first().category_id == 2
    #
    # @pytest.mark.django_db
    # def test_category_put(self, api_client: APIClient):
    #     url = 'http://localhost:8000/api/v1/category/update/3'
    #     response1 = api_client.put(url)
    #     response2 = api_client.put(url , data={"name" : "Home2"})
    #     assert response1.status_code == 400
    #     assert response1.json().get("name") == ["This field is required."]
    #     assert response2.status_code == 200
    #     assert response2.json().get("id") == 3
    #     assert response2.json().get("name") == "Home2"
    #
    # @pytest.mark.django_db
    # def test_category_patch(self, api_client: APIClient):
    #     url = 'http://localhost:8000/api/v1/category/update/3'
    #     response1 = api_client.patch(url)
    #     response2 = api_client.patch(url, data={"name": "Home2"})
    #     assert response1.status_code == 200
    #     assert response1.json().get("id") == 3
    #     assert response1.json().get("name") == "Home"
    #     assert response2.status_code == 200
    #     assert response2.json().get("id") == 3
    #     assert response2.json().get("name") == "Home2"
    #
    # @pytest.mark.django_db
    # def test_category_detail(self, api_client: APIClient):
    #     url1 = 'http://localhost:8000/api/v1/category/4'
    #     url2 = 'http://localhost:8000/api/v1/category/2'
    #     response1 = api_client.get(url1)
    #     response2 = api_client.get(url2)
    #     assert response1.status_code == 404
    #     assert response1.json().get("detail") == "No Category matches the given query."
    #     assert response2.status_code == 200
    #     assert "id" in response2.json().keys()
    #     assert "name" in response2.json().keys()
    #     assert response2.json().get("id") == 2
    #
    #

# django admin : media -> tg server
# file_id
