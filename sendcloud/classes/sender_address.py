import sendcloud
from sendcloud.http import Client


class SenderAddress(Client):
    def get_sender_addresses(self):
        """
        With this endpoint you can retrieve all the sender addresses that you have created under your account.

        :return:
        """

        url = sendcloud.BASE_URL + f"user/addresses/sender"

        response = self.get(url)

        return response.json()

    def get_single_sender_address(self, pk: str):
        """
        With this enpoint you can get a specific invoice that has been issued to your account.

        :param pk:
        :return:
        """

        url = sendcloud.BASE_URL + f"user/invoices/{pk}"

        response = self.get(url)

        return response.json()
