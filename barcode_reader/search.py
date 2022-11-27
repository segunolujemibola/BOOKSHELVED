from book_search import fetch_book_details
from collections import defaultdict


class Search:
    def __int__(self, isbn, gh):
        self.isbn = isbn

    def search_book(self):
        isbn_length = len(str(self.isbn))
        if isbn_length != 10 and isbn_length != 13:
            raise ValueError('ISBN length must be 10 or 13 characters')

        return fetch_book_details(self.isbn)

    def search_results(self):
        try:
            result = self.search_book()
        except ValueError as e:
            return e

        else:
            if result['status'] == 0:
                raise Exception(result['error'])
            else:
                data = result['data']
                tags = ['title', 'authors', 'publish_date', 'number_of_pages', 'publishers',
                        'isbn_10', 'isbn_13', 'physical_format',
                        'full_title', 'subtitle', 'notes', 'works', 'key', 'latest_revision', 'revision', 'subjects']

                book_info = {}
                for tag in tags:
                    try:
                        book_info[tag] = data[tag]
                    except KeyError:
                        book_info[tag] = "N/A"

                return book_info



