from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name, brand, max_speed, speed):
        self.name = name           
        self.brand = brand         
        self.max_speed = max_speed 
        self.speed = speed         

    @abstractmethod
    def tezlik(self):
        pass

class Malibu(Car):
    def __init__(self, name, brand, max_speed, speed):
        super().__init__(name, brand, max_speed, speed)
    
    def tezlik(self):
        return f"{self.name} {self.brand}: Maksimal tezlik - {self.max_speed} km/soat, 100 km/soat ga {self.speed} soniyada chiqadi"


malibu = Malibu("Malibu 2.0 Turbo", "Chevrolet", 215, 6.2)

print(malibu.tezlik())
