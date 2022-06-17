def test_setup_sendcloud():
    import sendcloud

    sendcloud.API_KEY = "TEST_API_KEY"
    sendcloud.API_SECRET = "TEST_SECRET"


def test_setup_sendcloud_with_parner_id():
    import sendcloud
    from sendcloud.http import Client

    sendcloud.API_KEY = "TEST_API_KEY"
    sendcloud.API_SECRET = "TEST_SECRET"
    sendcloud.PARTNER_ID = "10"

    client = Client()
    assert client._get_headers()["Sendcloud-Partner-Id"] is sendcloud.PARTNER_ID
