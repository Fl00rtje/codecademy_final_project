class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "Your are registered as user: {name}, email: {email}, books read: {books}.".format\
            (name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{name}, your email has been updated to: {email}".format(email=self.email, name=self.name))

    def read_book(self, book, rating=None):
        self.rating = rating
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        number_values = 0
        for key, value in self.books.items():
            number_values += 1
            sum += value
            average = sum / number_values
        return "I rated the books that I read with an average of: {average}.".format\
            (average=average)


    def __hash__(self):
        return hash((self.name, self.email))

    def get_books(self):
        for key, value in self.books.items():
            print("I read {key.title}, and gave it the rating {value}.".format(key=key, value=value))
            # This one returns none, that's not so pretty.
