from collections import namedtuple

# 1
Car = namedtuple('Car', ['model', 'make', 'color', 'year'])
class Cars(Car):
    def __new__(cls, model, make, color, year, price):
        return super().__new__(cls, model, make, color, year)

    def __init__(self, model, make, color, year, price):
        self.price = price

    def output(self):
        return f'Model: {car1.model}, \nMake: {car1.make}, \nColor: {car1.color}, \nYear: {car1.year}'


car1 = Cars('Tesla Roadster', 'Tesla', 'Black', 2023, '$30.000')
# print(car1.output())




#2
Books = namedtuple('Books', ["Title", 'Author', 'Genre', 'price'])
class Book(Books):
    def __new__(cls, Title, Author, Genre, Price, Pages):
        return super().__new__(cls, Title, Author, Genre, Price)

    def __init__(self, Title, Author, Genre, Price, Pages):
        self.Pages = Pages

    def output_book(self):
        return f'Title: {book1.Title}, \nAuthor: {book1.Author}, \nGenre: {book1.Genre}, \nPrice: {book1.price}, \nPages: {book1.Pages}'


book1 = Book('Harry Potter and half-blood prince', 'J.K.Rowling', 'book-series', '50.000', '320+')
# print(book1.output_book())

# 3
Phone = namedtuple('Phone', ('model', 'make', 'memory', 'color'))
class Smartphone(Phone):
    def __new__(cls, model, make, memory, color, price):
        return super().__new__(cls, model, make, memory, color)


    def __init__(self, model, make, memory, color, price):
        self.price = price

    def output_r(self):
        return f'Model: {p2.model}, \nMake: {p2.make}, \nMemory: {p2.memory}, \nColor: {p2.color}, \nPrice: {p2.price}'


p2 = Smartphone('Samsung A04e', 'Samsung', '32 GB', 'ocean blue', '$200')
# print(p2.output_r())


# 4
Student = namedtuple('Student', ['name', 'surname', 'age', 'university'])
class Students(Student):
    def __new__(cls, name, surname, age, university, major):
        return super().__new__(cls, name, surname, age, university)

    def __init__(self, name, surname, age, university, major):\
        self.major = major

    def output(self):
        return f'Name: {s1.name}, \nSurname: {s1.surname}, \nAge: {s1.age}, \nUniversity: {s1.university}, \nMajor: {s1.major}'

        
s1 = Students('Zarnigor', 'Dekhonova', 18, 'UzJMCU', 'International Relations')
print(s1.output())

