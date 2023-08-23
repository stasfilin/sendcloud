import sendcloud
from sendcloud.http import Client


class PickUp(Client):
    def get_pick_ups(self):
        """
        This endpoint will return all the pick ups requested by your account.
        If you want to change that behaviour please provide
        additional parameters which you can find under Query parameters.

        :return:
        """

        url = sendcloud.BASE_URL + "pickups"

        response = self.get(url)

        return response.json()

    def create_pick_up(self, data: dict):
        """
        This endpoint will create a pick up request for your account.
        Please read about the expected behaviour below.

        :param data: pick up data
        :return:
        """

        url = sendcloud.BASE_URL + "pickups"

        response = self.post(url, data)

        return response.json()
