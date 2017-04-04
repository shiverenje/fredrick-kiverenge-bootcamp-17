class Car(object):
    def __init__(self, type, name, model='GM'):
        self.type = type
        self.name = name
        self.model = model

    def speed(self):
        return 0

    def drive(self, speed):
        if self.name=='Truck':
            return 77
        else:
            return 1000

    def num_of_doors(self):
        li = ['Opel''Porshe', 'Koenigsegg']
        for k in li:
            if k == 'Opel':
                return 4
            elif k == 'Porshe':
                return 2
            elif k == 'Koenigsegg':
                return 2

    def num_of_wheels(self):
        if self.model == 'trailer':
            return 8
        else:
            return 4

    def is_saloon(self):
        if self.num_of_wheels() == 8:
            return 'Trailer'
        else:
            return 'Saloon'

    def car_speed(self):
        speed = {'parked_speed': 0, 'moving_speed': 77}

    def car_speed2(self):
        speedd = {'parked_speed': 0, 'moving_speed': 1000}


class moving_man(Car):
    pass


man = Car('MAN', 'Truck', 'trailer')
moving_man = man.drive(7)
moving_man_instance = isinstance(moving_man, Car)
moving_man_type = type(moving_man) is Car

print(moving_man_type)