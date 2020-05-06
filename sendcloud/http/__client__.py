import requests
import sendcloud

from typing import Any


class Client(object):
    client = requests.Session()

    def _get_headers(self):
        headers = {"Content-Type": "application/json"}
        return headers

    def post(self, url: str, data: Any[dict, list]) -> requests.Response:
        """
        Post request to API
        :param url: url
        :param data: post data
        :return: response object
        """
        response = self.client.post(
            url,
            data=data,
            auth=(sendcloud.API_KEY, sendcloud.API_SECRET),
            headers=self._get_headers(),
        )
        return response

    def get(self, url: str, query: dict) -> requests.Response:
        """
        Get request to API
        :param url: url
        :param query: get params
        :return: response object
        """
        response = self.client.get(
            url,
            params=query,
            auth=(sendcloud.API_KEY, sendcloud.API_SECRET),
            headers=self._get_headers(),
        )
        return response

    def put(self, url: str, data: Any[dict, list]) -> requests.Response:
        """
        Put request to API
        :param url: url
        :param data: put body
        :return: response object
        """
        response = self.client.put(
            url,
            data=data,
            auth=(sendcloud.API_KEY, sendcloud.API_SECRET),
            headers=self._get_headers(),
        )
        return response
