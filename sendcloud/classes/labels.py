import sendcloud
from sendcloud.http import Client


class Labels(Client):
    def get_labels(self, pk: str):
        """
        Get labels
        :param pk: label ID
        :return:
        """

        url = sendcloud.BASE_URL + f"labels/{pk}"

        response = self.get(url)

        return response.json()

    def bulk_pdf_label_printing(self, array):
        """
        Using this endpoint you may print your parcel labels in bulk.

        :param array: payload
        :return:
        """

        url = sendcloud.BASE_URL + f"labels"

        response = self.post(url, array)

        return response.json()
