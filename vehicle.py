class Vehicle:
    def __init__(self,brand,color,plate):
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0
    def acelerar(self):
            self.speed += 2
            print(f"El {self.brand} aceleró a {self.speed} km/h")
            
    def desacelerar(self):
        if self.speed >=10:
            self.speed -=10
        else:
            self.speed = 0
        print(f'el{self.brand}desaceleró a {self.speed} km/h')
#Creación de los objetos
my_vehicle = Vehicle('Hiunday','black','Pn88')
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.acelerar()