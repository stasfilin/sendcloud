import sendcloud
from sendcloud.http import Client


class IntegrationsAndOrders(Client):
    def get_integrations(self):
        """
        Retrieving your list of integrations

        :return:
        """

        url = sendcloud.BASE_URL + f"integrations"

        response = self.get(url)

        return response.json()

    def update_integrations(self, pk: str, array: dict):
        """
        You can update an integration’s settings through a PUT request to our Integration endpoint.

        :param array:
        :param pk:
        :return:
        """

        url = sendcloud.BASE_URL + f"integrations/{pk}"

        response = self.put(url, array)

        return response.json()

    def retrieving_shipments(self, pk: str, query: dict = None):
        """
        You’re able to retrieve the list of shipments from an integration
        (as seen in our product’s “Incoming Orders” area).
        Do note that these shipments will NOT be affected by Shipping Rules on the time of retrieval.
        This endpoint is paginated.
        Please navigate through the results by using the URLs provided within the “next” and “previous” fields.

        :param query: Query parameters
        :param pk: Shipment ID
        :return:
        """

        url = sendcloud.BASE_URL + f"integrations/{pk}/shipment"

        response = self.get(url, query)

        return response.json()

    def insert_shipments(self, pk: str, body: list):
        """
        You can insert shipments into an API integration.
        This is a more refined and supported way of creating shipments within our
        Panel which then can be used to generate Parcels easily.
        This endpoint has a way more relaxed validation than our
        Parcel API endpoint and is recommended for third party integrators.

        This is an UPSERT endpoint. This means that this endpoint tries to be idempotent given specific fields,
        updating our database values if there’s a match or creating a new entry if there is not.

        Our system will ensure uniqueness of shipments with the
        combination of external_order_id and external_shipment_id.

        The system will only update orders that have had their updated_at (ISO 8601 DateTime) timestamp changed.

        The field external_shipment_id is used to split orders across multiple shipments,
        this feature is not supported in all shop systems.
        However, if the shop has this feature and allows the distribution of the product items of an order across
        different shipments you can use the shipment data instead of plain order,
        and create multiples entries for each shipment. When the order is created and does not have any shipments yet,
        you can send external_shipment_id as null.

        If the shop does not multiple shipments per order, or you wish to only synchronize orders,
        this feature you can sent the external_shipment_id with null value.

        Batches are limited to 100 orders at once.

        :param pk:
        :param body:
        :return:
        """

        url = sendcloud.BASE_URL + f"integrations/{pk}/shipments"

        response = self.post(url, body)

        return response.json()

    def delete_orders(self, pk: str, body: dict):
        """
        If orders are cancelled or deleted in a shop you must remove them from our database
        (as the fields “order_status” and “payment_status” are not mapped to anything within our systems).
        You must provide either a shipment_uuid or
        the combination of external_order_id and external_shipment_id to this endpoint.

        :param body:
        :param pk:
        :return:
        """

        url = sendcloud.BASE_URL + f"integrations/{pk}/shipments/delete"

        response = self.post(url, body)

        return response.json()
