import requests_mock

from .testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import Users

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_get_current_user(self):
        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "user",
                json=self.get_fixture("user.json"),
            )

            user = Users().get_current_user()

            assert user["user"]["company_name"] == "Sendcloud"
