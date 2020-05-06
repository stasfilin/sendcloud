class Parcels(object):
    def get_parcels(self, query: dict):
        """
        BASE_URL + parcels
        :return:
        """
        pass

    def get_parcel(self, pk: str):
        """
        BASE_URL + parcels/{pk}
        :param pk:
        :return:
        """
        pass

    def create_parcel(self):
        """
        BASE_URL + parcels
        :return:
        """
        pass

    def update_parcel(self, pk: str):
        """
        BASE_URL + parcels

        :param pk:
        :return:
        """
        pass

    def return_portal_url(self, pk: str):
        """
        BASE_URL + parcels/{ID}/return_portal_url
        :return:
        """
        pass

    def get_parcel_documents(self, pk: str):
        """
        GET https://panel.sendcloud.sc/api/v2/parcels/{id}/documents/{type}

        :param pk:
        :return:
        """
        pass

    def get_parcels_statuses(self):
        """
        GET https://panel.sendcloud.sc/api/v2/parcels/statuses

        :return:
        """
