from book import Book
from user import User

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}".format(email))

    # I have a dictionary of books instead of a list.
    def add_user(self, name, email, books=None):
        self.users[email] = User(name, email)
        if books is not None:
            for book, rating in books.items():
                self.add_book_to_user(book, email, rating)


    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        return(max(self.books, key=self.books.get))

    def highest_rated_book(self):
        average_ratings_books = {}
        for book in self.books:
            average_ratings_books[book] = book.get_average_rating()
        print(max(average_ratings_books, key=average_ratings_books.get))

    def most_positive_user(self):
        pass
        average_ratings_user = {}
        for user in self.users.values():
            average_ratings_user[user] = user.get_average_rating()
        print(max(average_ratings_user, key=average_ratings_user.get))
