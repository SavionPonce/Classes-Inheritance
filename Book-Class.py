class Book:
    '''Book Class'''
    def __init__(self, title):
        self.__title = title
    
    @property
    def title(self):
        print('Getting Title')
        return self.__title
    
    @property
    def author(self):
        print('Getting Author')
        return self.__author
    
    @property
    def genre(self):
        print('Getting Genre')
        return self.__genre
    
    @property
    def publish_year(self):
        print('Getting Publish Year')
        return self.__publish_year
    
    @title.setter
    def title(self, new_title):
        print('Setting Title')
        self.__title = new_title

    @author.setter
    def author(self, new_author):
        print('Setting Author')
        self.__author = new_author
    
    @genre.setter
    def genre(self, new_genre):
        print('Setting Genre')
        self.__genre = new_genre

    @publish_year.setter
    def publish_year(self, new_publish_year):
        print('Setting Publish Year')
        self.__publish_year = new_publish_year
    
    def read(self):
        print('Reading')

class Textbook(Book):
    def study(self):
        print('Studying')

class Address_Book(Book):
    def search(self):
        print('Searching')