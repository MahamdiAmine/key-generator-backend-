import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from key.models import Key
from key.serializers import KeySerializer


# keys
class KeyApiTest(TestCase):
    """
    test the Keys
    """

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_key_list(self):
        # Test retrieving a list of keys
        Key.objects.create(
            name="KEY 1",
            key="PR001lv8628628 a",
        )
        Key.objects.create(
            name="KEY 2",
            key="PR001lv8628628 b",
        )

        response = self.client.get(reverse("key-list"))
        products = Key.objects.all().order_by("id")
        serializer = KeySerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_key(self):
        # test creating a new key
        key = {
            "name": "KEY 3",
            "key": "PR001lv828628 c",
        }

        self.client.post(reverse("key-list"), key)
        key_exist = Key.objects.filter(key=key["key"]).exists()
        self.assertTrue(key_exist)


class GetSingleKeyTest(TestCase):
    """
     Test module for GET single key API
    """

    def setUp(self):
        self.client = APIClient()

    def test_get_valid_single_key(self):
        key = Key.objects.create(
            name="Key",
            key="PR004kehvger gnkjhfi gb",
        )
        response = self.client.get(
            reverse("key-detail", kwargs={"pk": key.pk})
        )
        key_serializer = KeySerializer(key)
        self.assertEqual(response.data, key_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = self.client.get(
            reverse("key-detail", kwargs={"pk": 2021})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleProductTest(TestCase):
    """
     Test module for updating an existing product record
     """

    def setUp(self):
        self.client = APIClient()

    def test_valid_update_product(self):
        key = Key.objects.create(
            name="TEST_Key",
            key="F002_819_5046_540_ A",
        )
        updated_key = {
            "name": "Updated TEST_Key",
            "key": "F002_819_5046_540_ A",
        }
        response = self.client.put(
            reverse("key-detail", kwargs={"pk": key.pk}),
            data=json.dumps(updated_key),
            content_type="application/json"
        )
        self.assertEqual(response.data["name"], updated_key["name"])
        self.assertEqual(response.data["key"], updated_key["key"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_product(self):
        # test updating a key with invalid without a code
        invalid_key = {
            "name": "INVALID KEY!",
            "code": None,
        }
        key = Key.objects.create(
            name="TEST_Key",
            key="F002_819_5046_540_ A",
        )
        response = self.client.put(
            reverse("key-detail", kwargs={"pk": key.pk}),
            data=json.dumps(invalid_key),
            content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleKeyTest(TestCase):
    """
    Test module for deleting an existing key record
    """

    def setUp(self):
        self.client = APIClient()

    def test_valid_delete_key(self):
        key = Key.objects.create(
            name="Key",
            key="F003 681_861_682_566_ K",
        )
        response = self.client.delete(
            reverse("key-detail", kwargs={"pk": key.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_key(self):
        response = self.client.delete(
            reverse("key-detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
