
print("Map")

# Định nghĩa hàm bình phương
def square(x):
    return x * x
# Danh sách các số
numbers = [1, 2, 3, 4, 5]
# Áp dụng hàm square cho từng phần tử trong numbers
squared_numbers = map(square, numbers)
# Chuyển kết quả thành list và in ra
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


# Danh sách các số
numbers = [1, 2, 3, 4, 5]
# Áp dụng hàm lambda để bình phương từng phần tử
squared_numbers = map(lambda x: x * x, numbers)
# Chuyển kết quả thành list và in ra
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


# Hai danh sách số
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
# Áp dụng hàm lambda để cộng từng cặp phần tử từ hai danh sách
sum_list = map(lambda x, y: x + y, list1, list2)
# Chuyển kết quả thành list và in ra
print(list(sum_list))  # Output: [11, 22, 33, 44]


print("Dictionary")

# Khởi tạo dictionary rỗng
my_dict = {}
# Khởi tạo dictionary với các cặp key-value
student = {
    'name': 'An',
    'age': 20,
    'major': 'Computer Science'
}
# Sử dụng hàm dict()
person = dict(name='Bình', age=25, city='Hà Nội')


# Thêm phần tử mới
student['gpa'] = 3.8
# Cập nhật giá trị của key 'age'
student['age'] = 21
print(student)
# Output: {'name': 'An', 'age': 21, 'major': 'Computer Science', 'gpa': 3.8}


# Truy xuất giá trị bằng key
name = student['name']
print(name)  # Output: An
# Sử dụng phương thức get()
age = student.get('age')
print(age)  # Output: 21
# Truy xuất key không tồn tại bằng get() sẽ trả về None hoặc giá trị mặc định nếu được cung cấp
gpa = student.get('gpa', 'Chưa cập nhật')
print(gpa)  # Output: 3.8


# Xóa phần tử với key 'gpa'
del student['gpa']
# Xóa phần tử với key 'major' và lấy giá trị của nó
major = student.pop('major')
print(major)  # Output: Computer Science
# Xóa phần tử cuối cùng
last_item = student.popitem()
print(last_item)  # Output: ('age', 21)
# Xóa tất cả các phần tử
student.clear()
print(student)  # Output: {}