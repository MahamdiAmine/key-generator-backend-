from django.test import TestCase
from key.models import Key
from decouple import config
from datetime import date


class KeyTests(TestCase):
    """
    test the Key models
    """

    def setUp(self):
        # authentication
        user = config('auth_username')
        password = config('auth_password')
        self.client.login(username=user, password=password)
        creation_date = date(2021, 6, 2)

        # create an expired key
        self.expired_key = Key.objects.create(
            name="Test KEY 1",
            key="PR001lv8628628 b",
            creation_date=creation_date,
            life_duration=(date.today() - creation_date).days - 1,
        )

        # create an unexpired key
        self.alive_key = Key.objects.create(
            name="Test KEY 2",
            key="PR001lfbv8628628 b",
            creation_date=creation_date,
            life_duration=(date.today() - creation_date).days + 1,
        )

    # test the key expiration
    def test_expired_keys(self):
        self.assertTrue(self.expired_key.is_expired)
        self.assertFalse(self.alive_key.is_expired)
