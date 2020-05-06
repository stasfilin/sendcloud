class IntegrationsAndOrders(object):
    def get_integrations(self):
        """
        GET https://panel.sendcloud.sc/api/v2/integrations

        :return:
        """

    def update_integrations(self, pk: str, array: dict):
        """
        PUT https://panel.sendcloud.sc/api/v2/integrations/{id}

        :param array:
        :param pk:
        :return:
        """

    def retrieving_shipments(self, pk: str, query: dict):
        """
        GET https://panel.sendcloud.sc/api/v2/integrations/{id}/shipments

        :param query:
        :param pk:
        :return:
        """

    def insert_shipments(self, pk: str, body: list):
        """
        POST https://panel.sendcloud.sc/api/v2/integrations/{id}/shipments

        :param pk:
        :param body:
        :return:
        """

    def delete_orders(self, pk: str):
        """
        POST https://panel.sendcloud.sc/api/v2/integrations/{id}/shipments/delete

        :param pk:
        :return:
        """
