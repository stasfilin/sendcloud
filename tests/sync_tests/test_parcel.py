import requests_mock

from .testcase import SendcloudTestCase

import sendcloud
from sendcloud.classes import Parcels

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"


class TestParcels(SendcloudTestCase):
    def test_parcels(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "parcels",
                json=self.get_fixture("parcels.json"),
            )

            parcels = Parcels().get_parcels()

            assert parcels["parcels"][0]["id"] == 3172

    def test_parcel_by_id(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "parcels/3",
                json=self.get_fixture("parcel_3.json"),
            )

            parcel = Parcels().get_parcel("3")

            assert parcel["parcel"]["id"] == 22

    def test_create_parcel(self):

        new_parcel_data = {
            "parcel": {
                "name": "John Doe",
                "company_name": "Sendcloud",
                "address": "Insulindelaan 115",
                "house_number": "115",
                "city": "Eindhoven",
                "postal_code": "5642CV",
                "telephone": "+31612345678",
                "request_label": True,
                "email": "john@doe.com",
                "data": [],
                "country": "NL",
                "shipment": {
                    "id": 8,
                },
                "weight": "10.000",
                "order_number": "1234567890",
                "insured_value": 2000,
            }
        }

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "POST",
                sendcloud.BASE_URL + "parcels",
                json=self.get_fixture("create_parcel.json"),
            )

            parcel = Parcels().create_parcel(new_parcel_data)

            assert parcel["parcel"][0]["id"] == 3

    def test_create_parcels(self):

        list_of_parcels = {
            "parcels": [
                {
                    "name": "John Doe",
                    "company_name": "Sendcloud",
                    "address": "Insulindelaan 115",
                    "house_number": "115",
                    "city": "Eindhoven",
                    "postal_code": "5642CV",
                    "telephone": "+31612345678",
                    "request_label": True,
                    "email": "john@doe.com",
                    "data": [],
                    "country": "NL",
                    "shipment": {
                        "id": 8,
                    },
                    "weight": "10.000",
                    "order_number": "1234567890",
                    "insured_value": 2000,
                },
                {
                    "name": "John Doe",
                    "company_name": "Sendcloud",
                    "address": "Insulindelaan 115",
                    "house_number": "115",
                    "city": "Eindhoven",
                    "postal_code": "5642CV",
                    "telephone": "+31612345678",
                    "request_label": True,
                    "email": "john@doe.com",
                    "data": [],
                    "country": "NL",
                    "shipment": {
                        "id": 8,
                    },
                    "weight": "8.000",
                    "order_number": "1234567891",
                    "insured_value": 500,
                },
            ]
        }

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "POST",
                sendcloud.BASE_URL + "parcels",
                json=self.get_fixture("create_multiple_parcels.json"),
            )

            parcel = Parcels().create_parcel(list_of_parcels)
            assert len(parcel["parcels"]) == 2

    def test_update_parcel(self):

        properties_to_update = {
            "id": 3,
            "name": "Anna Tester",
            "company_name": "Summer Co",
            "request_label": True,
        }

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "PUT",
                sendcloud.BASE_URL + "parcels",
                json=self.get_fixture("update_parcel.json"),
            )

            parcel = Parcels().update_parcel(properties_to_update)

            assert parcel["parcel"][0]["id"] == 3

    def test_cancel_parcel(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "POST",
                sendcloud.BASE_URL + "parcels/3/cancel",
                json=self.get_fixture("cancel_parcel.json"),
            )

            parcel = Parcels().cancel_parcel("3")

            assert parcel["status"] == "cancelled"

    def test_return_portal_url(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "parcels/3/return_portal_url",
                json=self.get_fixture("return_portal_url.json"),
            )

            parcel = Parcels().return_portal_url("3")

            assert parcel["url"] == "http://mybrand.shipping-portal.com/initiate/"

    def test_parcel_statuses(self):

        with requests_mock.Mocker() as mocker:
            mocker.register_uri(
                "GET",
                sendcloud.BASE_URL + "parcels/statuses",
                json=self.get_fixture("parcel_statuses.json"),
            )

            parcel = Parcels().get_parcels_statuses()

            assert len(parcel) == 4
