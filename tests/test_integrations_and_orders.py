import requests_mock

from tests.testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import IntegrationsAndOrders

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_integrations(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "integrations",
                json=self.get_fixture("integrations.json"),
            )

            integrations = IntegrationsAndOrders().get_integrations()

            assert integrations[0]["id"] == 1

    def test_update_integrations(self):
        data = {
            "shop_name": "API Integration",
            "shop_url": "https://www.google.com",
            "service_point_enabled": False,
            "service_point_carriers": [],
            "webhook_active": False,
            "webhook_url": "",
        }
        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "PUT",
                sendcloud.BASE_URL + "integrations/1",
                json=self.get_fixture("update_integration.json"),
            )

            integrations = IntegrationsAndOrders().update_integrations("1", data)

            assert integrations["system"] == "api"

    def test_retrieving_shipments(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "integrations/1/shipment",
                json=self.get_fixture("shipment_1.json"),
            )

            integrations = IntegrationsAndOrders().retrieving_shipments("1")

            assert integrations["results"][0]["integration"] == 1

    def test_insert_shipments(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "POST",
                sendcloud.BASE_URL + "integrations/1/shipments",
                json=self.get_fixture("shipments_response.json"),
            )

            integrations = IntegrationsAndOrders().insert_shipments(
                "1", self.get_fixture("shipments_request.json")
            )

            assert integrations[0]["external_order_id"] == "123456"

    def test_delete_orders(self):

        payload = {"external_order_id": "123457", "external_shipment_id": "S00002"}

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "POST", sendcloud.BASE_URL + "integrations/1/shipments/delete", json={},
            )

            integrations = IntegrationsAndOrders().delete_orders("1", payload)

            assert integrations == {}
