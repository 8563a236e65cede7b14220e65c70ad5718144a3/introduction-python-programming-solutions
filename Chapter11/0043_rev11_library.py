"""
Review Question 11
Create a class called library with data attributes like acc_number,
publisher, title and author. The methods of the class should include
    a) read() - acc_number, publisher, title, author
    b) compute() - accept umber of days late, calculate and display
       fine charged at rate of $1.50 per day
    c) display the data
"""


class Library:
    def __init__(self):
        self.acc_number = 0
        self.publisher = ""
        self.title = ""
        self.author = ""

    def read(self, acc_number, publisher, title, author):
        self.acc_number = acc_number
        self.publisher = publisher
        self.title = title
        self.author = author

    def compute(self, days_late):
        print(f"The late fee is ${1.5 * days_late}")

    def display(self):
        print(f"Author = {self.author}\n"
              f"Publisher = {self.publisher}\n"
              f"Title = {self.title}\n"
              f"Acc_Number = {self.acc_number}")


def main():
    library = Library()
    library.read(1234, "Packt", "Hello", "World")
    library.compute(6)
    library.display()


if __name__ == "__main__":
    main()

