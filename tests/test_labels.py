import requests_mock

from tests.testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import Labels

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_specific_label(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "labels/3172",
                json=self.get_fixture("labels_3172.json"),
            )

            label = Labels().get_labels("3172")

            assert (
                label["label"]["label_printer"]
                == "https://panel.sendcloud.sc/api/v2/label/label_printer/3172?hash=bbfd669ee9ebb19408b85b33d181a50040fd9bc4"
            )

    def test_bulk_pdf_label_printing(self):
        payload = {"label": {"parcels": [3172, 3171]}}
        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "POST",
                sendcloud.BASE_URL + "labels",
                json=self.get_fixture("labels.json"),
            )

            label = Labels().bulk_pdf_label_printing(payload)

            assert (
                label["label"]["label_printer"]
                == "https://panel.sendcloud.sc/api/v2/label/label_printer/?ids=3172,3171&hash=12a78fcd752a3764c4cb8d68f57cf045c916a7dd"
            )
