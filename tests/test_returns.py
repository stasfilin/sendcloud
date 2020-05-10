import requests_mock

from tests.testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import Returns

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_returns(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "returns",
                json=self.get_fixture("returns.json"),
            )

            returns = Returns().get_returns()

            assert returns["returns"][0]["id"] == 3

    def test_specific_return(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "returns/3",
                json=self.get_fixture("return_3.json"),
            )

            returns = Returns().get_return("3")

            assert returns["id"] == 3
