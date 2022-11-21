import requests


def fetch_book_details(isbn):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + str(isbn)

    response = requests.get(url)
    print(response.status_code)
    print(response.text)


fetch_book_details(9780781412148)
