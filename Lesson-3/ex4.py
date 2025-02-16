# Đa kế thừa - cho phép một lớp kế thừa từ nhiều lớp cha cùng lúc
class Flyable:
    def fly(self):
        print("Flyable")

class Swimable:
    def swim(self):
        print("Swimable")

class Duck(Flyable, Swimable):
    pass

duck = Duck()
duck.fly()
duck.swim()