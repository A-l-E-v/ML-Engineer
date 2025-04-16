# Создайте простую систему для учета книг в библиотеке,
# содержащую два класса: класс Book для представления
# книги и класс Library для управления коллекцией книг.
# Класс Book содержит атрибуты title, author и published_year
# (название книги, автор книги, год публикации книги).
# Класс Library хранит список книг. У него должны быть методы
# для добавления новой книги, удаления книги по названию,

# и вывода списка всех книг в библиотеке.Создайте несколько экземпляров книг и библиотеки, и проведите
# операции добавления, удаления и вывода книг.

class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
    
    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.published_year})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Книга {book.title} добавлена в библиотеку")
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга {title} удалена из библиотеки")
                return
        print(f"Книга {title} не найдена")
    
    def list_books(self):
        if not self.books:
            print("Библиотека пуста")
        else:
            print("Книги в библиотеке:")
            for book in self.books:
                print(book)

# Пример использования
lib = Library()
book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("1984", "Джордж Оруэлл", 1949)

lib.add_book(book1)
lib.add_book(book2)
lib.list_books()
lib.remove_book("1984")
lib.list_books()