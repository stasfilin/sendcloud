import sendcloud
from sendcloud.http import Client


class Invoices(Client):
    def get_invoices(self):
        """
        With this enpoint you can get all the invoices that have been issued to your account.

        :return:
        """

        url = sendcloud.BASE_URL + f"user/invoices"

        response = self.get(url)

        return response.json()

    def get_invoice(self, pk: str, query: dict = None):
        """
        With this enpoint you can get a specific invoice that has been issued to your account.

        :param query: Query parameters
        :param pk:
        :return:
        """

        url = sendcloud.BASE_URL + f"user/invoices/{pk}"

        response = self.get(url, query)

        return response.json()
