import sendcloud
from sendcloud.http import Client


class Returns(Client):
    def get_returns(self):
        """
        This endpoint retrieves all returns, both created through the return portal or the API.
        Depending on whether a return parcel contains items or not, the refund, reason,
        and message fields will be filled either in the return data, or the incoming parcel item data.
        :return:
        """

        url = sendcloud.BASE_URL + "returns"

        response = self.get(url)

        return response.json()

    def get_return(self, pk: str):
        """
        This endpoint retrieves a specific return from your account based on ID.
        Depending on whether a return parcel contains items or not, the refund, reason,
        and message fields will be filled either in the return data, or the incoming parcel item data.
        :param pk: return ID
        :return:
        """

        url = sendcloud.BASE_URL + f"returns/{pk}"

        response = self.get(url)

        return response.json()
