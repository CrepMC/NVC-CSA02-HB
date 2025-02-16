class Animal:
    className = "Animal"
    def __init__(self, type, color):
        self.type = type
        self.color =  color
    def make_sound(self):
        print("Animal make sound!!!")

class Dog(Animal):
    def __init__(self, type, color, sound):
        super().__init__(type, color)
        self.sound = sound
    def make_sound(self): # override lại phương thức của lớp cha
        print(f"This {self.type} make {self.sound}")
    
begie = Dog('Dog', 'White', "Woof")
begie.make_sound()
