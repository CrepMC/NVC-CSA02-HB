class Animal:
    className = "Animal"
    # Hàm init dùng để khởi tạo các thuộc tính của đối tượng
    def __init__(self, type, color): #init - khởi tạo
        self.type = type
        self.color = color

    #Định nghĩa phương thức make_sound cho đối tượng
    def make_sound(self):
        print("Animal make sound!!!")
        
# Animal là một lớp
# type and color là thuộc tính
# make_sound() là phương thức

dog = Animal("Dog", "Brown")
cat = Animal("Cat", "Orange")
# Có thể tạo vô số đối tượng của một lớp

print(dog.color)
print(cat.type)

cat.make_sound()