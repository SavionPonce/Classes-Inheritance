class Animal:
    '''Animal Class'''
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('Getting Name')
        return self.__name

    @property
    def species(self):
        print('Getting Species')
        return self.__species
    
    @property
    def age(self):
        ('Getting Age')
        return self.__age
    
    @name.setter
    def name(self, new_name):
        print('Setting Name')
        self.__name = new_name

    @species.setter
    def species(self, new_species):
        print('Setting Species')
        self.__species = new_species
    
    @age.setter
    def age(self, new_age):
        print('Setting Age')
        self.__species = new_age
    
    def move(self):
        print('Moving')

    def eat(self):
        print('Eating')

class Fish(Animal):
    def swim(self):
        print('Swimming')

class Snake(Animal):
    def hiss(self):
        print('Hissing')

class Person(Animal):
    def talk(self):
        print('Talking')