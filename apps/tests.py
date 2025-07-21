from unicodedata import category

import pytest
from django.contrib.auth.models import User

from apps.models import *
from rest_framework.test import APIClient


class TestCategory:
    @pytest.fixture
    def api_client(self):
        Category.objects.create(name='Sport')

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

    @pytest.mark.django_db
    def test_category_delete(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/delete1'
        response = api_client.delete(url)
        assert response.status_code == 204

    @pytest.mark.django_db
    def test_category_delete(self, api_client: APIClient):
        url = 'http://localhost:8000/api/v1/category/delete1'
        response = api_client.delete(url)
        assert response.status_code == 204



    

    # category / update < int: id >

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
