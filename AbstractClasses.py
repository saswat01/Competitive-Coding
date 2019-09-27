from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.price = price
        self.title = title
        self.author = author
    def display(self):
        if self.title:
            print("Title: "+self.title)
        else:
            print("Title: $title")
        if self.author:
            print("Author: "+self.author)
        else:
            print("Author: $author")
        if self.price:
            print("Price: {}".format(price))
        else:
            print("Price: $price")
            
    
    

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()