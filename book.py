class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "Title: '{title}', ISBN: {isbn}".format\
            (title=self.title, isbn=self.isbn)

    def __eq__(self, other_user):
        if self.title == other_user.title and self.isbn == other_user.isbn:
            return True
        else:
            return False

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Your ISBN has been updated to: {isbn}".format(isbn=self.isbn))

    def add_rating(self, rating):
        if rating in range(6):
            self.ratings.append(rating)
        else:
            print("This is an invalid rating.")

    def get_average_rating_book(self):
        average_rating = sum(self.ratings) / len(self.ratings)
        return "The average rating for '{title}' is: {average_rating}.".format\
          (title=self.title, average_rating=average_rating)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_ratings(self):
        ratings = self.ratings
        return "The ratings for '{title}' are: {ratings}".format\
          (title=self.title, ratings=ratings)
