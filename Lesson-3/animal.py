class Animal:
    # Thuộc tính của lớp
    className = "Animal"
    # Hàm init dùng để khởi tạo các thuộc tính của đối tượng
    def __init__(self, type, color): # initial - khởi tạo
        self.type = type
        self.color =  color
    # Định nghĩa phương thức make_sound cho đối tượng
    def __make_sound(self):
        print("Animal make sound!!!")

# Animal là một lớp
# type và color là thuộc tính 
# make_sound() là phương thức


