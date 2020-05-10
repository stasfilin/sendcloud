import sendcloud
from sendcloud.http import Client
from sendcloud.http.exceptions import ParcelNotFound


class Parcels(Client):
    def get_parcels(self, query: dict = None):
        """
        This endpoint retrieves all parcels which you have imported under your provided API credentials.
        You may filter parcels on the query parameters provided below.

        :param query:
        :return:
        """
        url = sendcloud.BASE_URL + "parcels"

        response = self.get(url, query)

        return response.json()

    def get_parcel(self, pk: str):
        """
        This endpoint retrieves a specific parcel from your account based on parcel id.


        :param pk: parcel id
        :return:
        """
        url = sendcloud.BASE_URL + f"parcels/{pk}"
        response = self.get(url)
        if response.status_code == 404:
            raise ParcelNotFound("No Parcel matches the given query.")
        return response.json()

    def create_parcel(self, data: dict):
        """
        This endpoint creates a parcel under your user, for which you can request a label immediately.
        In order to create a parcel you have to pass some additional arguments in JSON format
        within the object of parcel as you can see in the example on the right.

        :param data: Parcel Object
        :return:
        """

        url = sendcloud.BASE_URL + "parcels"
        response = self.post(url, data)
        return response.json()

    def update_parcel(self, data: dict):
        """
        This endpoint updates a parcel with the option to request a label - if it hasn’t been requested before.
        The post request parameters have to be nested under a parcel object.
        You can change any properties given in the Create parcel example under Post request parameters.
        :param data: parcel data
        :return:
        """

        url = sendcloud.BASE_URL + "parcels"
        response = self.put(url, data)
        return response.json()

    def cancel_parcel(self, pk: str):
        """
        This endpoint updates a parcel with the option to request a label for it if it hasn’t been requested before.
        Mind that the post request parameters have to be nested under a parcel object.
        You can change any properties given in the Create parcel example under Post request parameters.
        :param pk: parcel ID
        :return:
        """

        url = sendcloud.BASE_URL + f"parcels/{pk}/cancel"
        response = self.post(url)
        return response.json()

    def return_portal_url(self, pk: str):
        """
        This endpoint returns the url to the return portal for a parcel.
        If there is no brand connected to the parcel or no return portal is configured,
        this endpoint returns a status code 404.

        :param pk:
        :return:
        """
        url = sendcloud.BASE_URL + f"parcels/{pk}/return_portal_url"
        response = self.get(url)
        return response.json()

    def get_parcel_documents(self, pk: str, document_type: str):
        """
        The resolution of the returned document can be changed as well,
        this can be done by passing a dpi request argument.
        The table below gives an overview of the supported DPI and default value per file format.
        :param pk:
        :param document_type:
        :return:
        """

        url = sendcloud.BASE_URL + f"parcels/{pk}/documents/{document_type}"
        response = self.get(url)
        return response.json()

    def get_parcels_statuses(self):
        """
        This endpoint will return all possible parcel statuses.

        :return:
        """

        url = sendcloud.BASE_URL + f"parcels/statuses"
        response = self.get(url)
        return response.json()
