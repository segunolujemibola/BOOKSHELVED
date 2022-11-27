import requests
from errors import BookNotFoundError


def fetch_book_details(isbn: int):
    """
    fetch_book_details function searches for book information by ISBN.
    It uses the request module and the openlibrary API.

    Parameters
    ----------
    isbn : int

    Returns
    -------
    data : dict

    """

    url = f'https://openlibrary.org/isbn/{isbn}.json'
    response = requests.get(url)
    try:
        if response.status_code != 200:
            raise BookNotFoundError('The book you\'re looking for cannot be found, check ISBN and try again')
        data = response.json()
    except BookNotFoundError as error:
        return {'status': 0, 'error': error, 'data': None}

    else:
        return {'status': 1, 'error': None, 'data': data}


