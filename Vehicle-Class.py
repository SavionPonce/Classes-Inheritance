class Vehicle:
    '''Vehicle Class'''
    def __init__(self, model):
        self.__model = model
    
    @property
    def model(self):
        print('Getting Model')
        return self.__model

    @property
    def brand(self):
        print('Getting Brand')
        return self.__brand

    @property
    def year(self):
        print('Getting Year')
        return self.__year
    
    @property
    def license_plate(self):
        print('Getting License Plate')
        return self.__license_plate
    
    @model.setter
    def model(self, new_model):
        print('Setting Model')
        self.__model = new_model

    @brand.setter
    def brand(self, new_brand):
        print('Setting Brand')
        self.__brand = new_brand
    
    @year.setter
    def year(self, new_year):
        print('Setting Year')
        self.__year = new_year

    @license_plate.setter
    def license_plate(self, new_license_plate):
        print('Setting License Plate')
        self.__license_plate = new_license_plate
    
    def start_engine(self):
        print('Starting Engine')
    
    def accelerate(self):
        print('Accelerating')

    def reverse(self):
        print('Reversing')
    
    def brake(self):
        print('Braking')
    
    def turn(self):
        print('Turning')
    
    def turnoff_engine(self):
        print('Turning off Engine')

class Car(Vehicle):
    def drive(self):
        print('Driving')
    
class Bicycle(Vehicle):
    def ride(self):
        print('Riding')

class Boat(Vehicle):
    def sail(self):
        print('Sailing')

class Hot_air_Balloon(Vehicle):
    def float(self):
        print('floating')