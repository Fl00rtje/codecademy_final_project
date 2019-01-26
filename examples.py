# import user
from user import User
from book import Book
from fiction import Fiction
from non_fiction import NonFiction
from tome_rater import TomeRater

print("=====ADD USER=====")
floor = User("Floor Harmsen", "floor.harmsen@gmail.com")
print(floor)

print("=====UPDATE USER'S EMAIL=====")
floor.change_email("harmsen@gmail.com")

print("=====SEE USER'S DETAILS=====")
print(floor)

print("=====ADD BOOKS=====")
otje = Book("Otje", 1234567890)
google = Book("What would Google do?", 987654231)
marching_powder = Book("Marching Powder", 567891234)
print(otje)
print(google)

print("=====ADDING & SHOWING RATINGS FOR BOOKS=====")
otje.add_rating(4)
otje.add_rating(3)
otje.add_rating(2)
otje.add_rating(6)
print(otje.get_ratings())
print(otje.get_average_rating_book())

google.add_rating(5)
google.add_rating(3)
google.add_rating(2)
print(google.get_ratings())
print(google.get_average_rating_book())

print("=====ADDING A FICTION BOOK=====")
murder_on_5th_avenue = Fiction("Murder on 5th Avenue", "Aghata Christie", 987654321)
print(murder_on_5th_avenue)

print("=====ADDING A NON-FICTION BOOK=====")
microeconomic_theory = NonFiction("Microeconomic Theory", "Economics", "beginner", "12345")
print(microeconomic_theory)

print("=====NOW I CAN MARK THE BOOKS AS READ AND RATE THEM=====")
floor.read_book(otje, 4)
floor.read_book(google, 4)
floor.read_book(marching_powder, 2)
print(floor.get_books())
print(floor.get_average_rating())


# print("=====TOMERATOR=====")
# tome_rater_1 = TomeRater()
# tome_rater_1.create_book("Just another book", 12345678)
# #print(tome_rater_1)
# tome_rater_1.add_book_to_user(otje, "harmsen1@gmail.com", 3)
# tome_rater_1.add_book_to_user(otje, "harmsen@gmail.com", 3)
# tome_rater_1.add_book_to_user(marching_powder, "harmsen@gmail.com", 4)
# print(tome_rater_1.books)
# tome_rater_1.add_user("Tom", "tom@gmail.com", {google: 3, marching_powder: 4})
# tome_rater_1.add_user("Tom", "tom@gmail.com")
# tome_rater_1.add_book_to_user(otje, "tom@gmail.com", 4)
# print(tome_rater_1.users)

# print("=====ANALYSIS METHODS=====")
# print(tome_rater_1.print_catalog())
# print(tome_rater_1.print_users())
# print(tome_rater_1.most_read_book())
# print(tome_rater_1.highest_rated_book())
# print(tome_rater_1.most_positive_user())


# print("=====TESTING=====")
# D = {1:'a', 5:'b', 2:'a', 7:'a'}
# for key in D.keys():
#     print(key)

# mydict = {'A':4,'B':10,'C':0,'D':87}
# maximum = max(mydict, key=mydict.get)
# print(maximum, mydict[maximum])

# d= {'a':2,'b':5,'c':3}
# print(max(d, key=d.get))
