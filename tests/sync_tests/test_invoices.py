import requests_mock

from .testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import Invoices

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_get_invoices(self):
        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "user/invoices",
                json=self.get_fixture("invoices.json"),
            )

            invoices = Invoices().get_invoices()

            assert invoices["invoices"][0]["id"] == 1

    def test_specific_invoice(self):
        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "user/invoices/1",
                json=self.get_fixture("invoice_1.json"),
            )

            invoices = Invoices().get_invoice("1")

            assert invoices["invoice"]["id"] == 1
