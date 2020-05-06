import hmac
import json


class WebHooks(object):
    API_SECRET: str

    def payload_validation(self, data: dict):
        """
        https://docs.sendcloud.sc/api/v2/shipping/#payload-validation-1

        :param api_secret:
        :param data:
        :return:
        """

        message = json.dumps(data)
        signature = hmac.new(
            key=self.API_SECRET.encode("utf-8"),
            msg=message.encode("utf-8"),
            digestmod="sha256",
        )
        return signature.hexdigest()

    def _get_headers(self, signature: str):
        """
        https://docs.sendcloud.sc/api/v2/shipping/#webhook-request

        :param signature:
        :return:
        """

        headers = {"Sendcloud-Signature": signature, "Content-Type": "application/json"}

        return headers

    def webhook_request(self):
        pass
