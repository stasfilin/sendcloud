import requests_mock

from tests.testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import SenderAddress

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_get_sender_address(self):
        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "user/addresses/sender",
                json=self.get_fixture("sender_addresses.json"),
            )

            sender_addresses = SenderAddress().get_sender_addresses()

            assert sender_addresses["sender_addresses"][0]["id"] == 2

    def test_single_sender_address(self):
        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "user/invoices/1",
                json=self.get_fixture("sender_address_1.json"),
            )

            sender_addresses = SenderAddress().get_single_sender_address("1")

            assert sender_addresses["sender_address"]["id"] == 1
