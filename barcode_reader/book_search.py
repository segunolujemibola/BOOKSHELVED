import requests


def fetch_book_details(isbn:int):
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
    status = None
    url = f'https://openlibrary.org/isbn/{isbn}.json'
    isbn_length = len(str(isbn))
    if isbn_length != 10 and isbn_length != 13:
        raise ValueError('ISBN length must be 10 or 13 characters')
    response = requests.get(url)
    try:
        data = response.json()
    except Exception as e:
        status = 'Failed'
        if response.status_code == 404:
            print('The book you\'re looking for cannot be found')
        else:
            print(e)
    else:
        status = 'Success'
        return data
    finally:
        print(status)

