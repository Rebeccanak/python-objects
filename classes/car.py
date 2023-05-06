class Car:
    fuel_type = "Gaseline"

    def __init__(self,make,model,color):
        self.make = make
        self.model =model
        self.color = color

    def hoot(self):
        return f"The {self.make} {self.model} {self.color} is pee peeing uses{self.fuel_type} " 

    def start(self):
        return f"The {self.make} {self.model} {self.color} is driving on the road " 
    def park(self):
        return f"The {self.color} {self.model} is parking in the field"          