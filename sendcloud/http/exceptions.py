class RateLimitingException(Exception):
    """
    Requests to our API are limited on a per Sendcloud account basis.
    If you have multiple API keys per Sendcloud account, the budget is shared between these keys.
    If you get rate limited, we return an empty response with HTTP status code 429.
    """


class NotFound(Exception):
    """
    ERROR CODE: 404
    DESCRIPTION: The resource you are looking for can not be found
    """


class RequestThrottled(Exception):
    """
    ERROR CODE: 429
    DESCRIPTION: Your requests are being throttled, slow down
    """


class ParcelCannotBeRequested(Exception):
    """
    ERROR CODE: 300
    DESCRIPTION: Parcel cannot be requested. This may be due to missing shipping method or shipping country ids.
    SUGGESTED SOLUTION: Provide a valid shipping method / shipping country in your POST requests’ data
    """


class ParcelNotFound(Exception):
    """
    ERROR CODE: 404
    DESCRIPTION: Parcel is not found with ID: {id}
    """


class ParcelNotBeChanged(Exception):
    """
    ERROR CODE: 405
    DESCRIPTION: An announced parcel may not be changed.
    SUGGESTED SOLUTION: Cancel the parcel if possible and create a new one.s
    """


class ParcelIdIsMissing(Exception):
    """
    ERROR CODE: 500
    DESCRIPTION: Parcel ID is missing. Process is being terminated.
    SUGGESTED SOLUTION: Provide a legitimate Parcel ID in your request
    """


class InvalidParcelInformation(Exception):
    """
    ERROR CODE: 500
    DESCRIPTION: You didn’t pass any parcel information. Process is being terminated.
    SUGGESTED SOLUTION: Make sure your request and the data you are trying to pass are valid.
    """


class CantGetParcelIDs(Exception):
    """
    ERROR CODE: 300
    DESCRIPTION: Can’t get the Parcel IDs (must be comma seperated)
    SUGGESTED SOLUTION: Make sure the requested Parcel ID’s exist and are comma separated
    """


class InvalidHash(Exception):
    """
    ERROR CODE: 300
    DESCRIPTION: Hash is invalid
    SUGGESTED SOLUTION: Make sure you didn’t modify the hash
    """
