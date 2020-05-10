import sendcloud
from sendcloud.http import Client


class ShippingMethods(Client):
    def get_shipping_methods(self):
        """
        This endpoint will return the shipping methods that are associated with your default sender address.
        If you want to change that behaviour please provide
        additional parameters which you can find under Query parameters.

        :return:
        """

        url = sendcloud.BASE_URL + "shipping_methods"

        response = self.get(url)

        return response.json()

    def get_shipping_method(self, pk: str, query: dict = None):
        """
        This individual shipping method endpoint will provide you with a single
        detailed shipping method information based on the id that you request.
        This endpoint works based on your default sender address which extends to the behaviour written below:

        Please read about the expected behaviour below.
        If you have sender addresses in multiple countries,
        this means you have to set a default carrier service for each country.
        Take Colissimo and PostNL as an example - If your default sender address is set to the country of Netherlands,
        you will not be able to retrieve the Colissimo shipping method by providing its ID.
        This occurs when a sender address in France is not provided in the parameter.
        :param query: query parameters
        :param pk:
        :return:
        """

        url = sendcloud.BASE_URL + f"shipping_methods/{pk}"

        response = self.get(url, query)

        return response.json()
