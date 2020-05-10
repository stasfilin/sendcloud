import requests_mock

from tests.testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import Brands

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_brands(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "brands",
                json=self.get_fixture("brands.json"),
            )

            brands = Brands().get_brands()

            assert brands["brands"][0]["id"] == 1

    def test_specific_brand(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "brand/3",
                json=self.get_fixture("brand_3.json"),
            )

            brand = Brands().get_brand("3")

            assert brand["id"] == 1
