import datetime

class Vehicle(object):
    num_of_wheels = 4
    milage = 0
    manufacturer = 'Toyota'

    def __init__(self):
        self.manufacturer = Vehicle.manufacturer
        self.milage = Vehicle.milage
        self.num_of_wheels = Vehicle.num_of_wheels
    def get_year(self):
        t =datetime.datetime.now()
        return t


class Nissan(Vehicle):
    def getVin(self):
        v = str(input('Enter the vehicle identification number '))
        return v

    def set_selling_price(self):
        s = str(input('How much would like to sell the nissan '))
        return s

    def get_wheels_number(self):
        return self.num_of_wheels

    def get_manufacturer(self):
        return self.manufacturer

    def show_date(self):
        return Vehicle.get_year(self)


class car(Vehicle):
    def getVin(self):
        v = str(input('please enter the vehicle identification number '))
        return v

    def get_wheels_number(self):
        return self.num_of_wheels

    def get_manufacturer(self):
        return self.manufacturer

    def set_selling_price(self):
        s = str(input('How much are you selling the car '))
        return s
    def show_date(self):
        return Vehicle.get_year(self)



d = car()
print(d.getVin())
print(d.get_wheels_number())
print(d.get_manufacturer())
print(d.show_date())
