import json
import os


class SendcloudTestCase(object):
    def get_fixture(self, filename: str):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        f = os.path.join(__location__, "fixtures", filename)
        with open(f) as json_file:
            data = json.load(json_file)
            return data
