class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
 
    def display_info(self):
        print(f"{self.make} {self.model}")