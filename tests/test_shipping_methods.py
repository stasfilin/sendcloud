import requests_mock

from tests.testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import ShippingMethods

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_shipping_methods(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "shipping_methods",
                json=self.get_fixture("shipping_methods.json"),
            )

            shipping_methods = ShippingMethods().get_shipping_methods()

            assert shipping_methods["shipping_methods"][0]["carrier"] == "carrier_code"

    def test_specific_shipping_method(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "shipping_methods/8",
                json=self.get_fixture("shipping_method_8.json"),
            )

            returns = ShippingMethods().get_shipping_method("8")

            assert returns["shipping_method"]["carrier"] == "sendcloud"
            assert returns["shipping_method"]["id"] == 8
