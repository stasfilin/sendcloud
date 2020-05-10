import sendcloud
from sendcloud.http import Client


class Brands(Client):
    def get_brands(self):
        """
        This endpoint retrieves all brands.

        :return:
        """

        url = sendcloud.BASE_URL + "brands"

        response = self.get(url)

        return response.json()

    def get_brand(self, pk: str):
        """
        This endpoint retrieves a specific brand from your account based on id.

        :param pk: brand ID
        :return:
        """

        url = sendcloud.BASE_URL + f"brand/{pk}"

        response = self.get(url)

        return response.json()
