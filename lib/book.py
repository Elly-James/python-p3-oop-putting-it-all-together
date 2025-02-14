#!/usr/bin/env python3

class Book:
    def __init__(self, title="River and the Source", page_count=90):
     
        if isinstance(title, str) and 1 <= len(title) <= 100:
            self._title = title
        else:
            print("Title must be string between 1 and 100 characters.")
            self._title = "Unknown"

        if isinstance(page_count, int) and page_count > 0:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            self._page_count = 1

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str) and 1 <= len(title) <= 100:
            self._title = title
        else:
             print("Title must be string between 1 and 100 characters.")

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
       if isinstance(page_count, int) and page_count> 0:
            self._page_count = page_count
       else:
            print("page_count must be an integer")
            self._page_count = "Unknown"

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

   
    title = property(get_title, set_title)
    page_count = property(get_page_count, set_page_count)

book = Book()
print(book.title)  
print(book.page_count)  

book.title = "Rich Dad Poor Dad"
book.page_count = 200
print(book.title)
print(book.page_count)

book.title = "Dholuo Mit"
book.page_count = -30
print(book.title)
print(book.page_count)
