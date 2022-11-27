class Error(Exception):
    """ Base class for other exceptions"""
    pass


class BookNotFoundError(Error):
    """ Raised when the response data is empty"""
    pass


class RequestError(Error):
    """ Raised when the get request returns any status code other than 200"""
    pass

