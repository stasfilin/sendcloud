import sendcloud
from sendcloud.http import Client
from sendcloud.types import JSONType


class Users(Client):
    def get_current_user(self) -> JSONType:
        """
        With this endpoint you can request the data that is connected with your own user.

        :return:
        """

        url = sendcloud.BASE_URL + f"user"

        response = self.get(url)

        return response.json()
