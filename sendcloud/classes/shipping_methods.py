class ShippingMethods(object):
    def get_shipping_methods(self):
        """
        GET https://panel.sendcloud.sc/api/v2/shipping_methods

        :return:
        """

    def get_shipping_method(self, pk: str, sender_address: str, service_point_id: str):
        """
        GET https://panel.sendcloud.sc/api/v2/shipping_methods/{id}?sender_address={sender_address}&service_point_id={service_point_id}

        :param pk:
        :param sender_address:
        :param service_point_id:
        :return:
        """
