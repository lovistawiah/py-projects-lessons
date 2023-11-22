# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # TODO: add properties
        # hidden attribute of a class
        self.__secret = "This is a secret"

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def get_discount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", 'Lovis', 233, 14.9)
b2 = Book("The Catcher in the Rye", 'Lovis', 233, 14.9)

# TODO: print the price of book1
print(b1.get_price())

# TODO: try setting the discount
print(b1.get_price())
b1.get_discount(0.10)
print("Discount:", b1.get_price())

# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)