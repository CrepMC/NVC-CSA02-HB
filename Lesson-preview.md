# VI. Thuật toán tìm kiếm
## 1. Tìm kiếm tuần tự (Linear Search):
#### Ý tưởng: 
Duyệt tuần tự qua từng phần tử trong danh sách cho đến khi tìm thấy phần tử cần tìm.
Ví dụ Python: Tìm kiếm tuần tự (Linear Search):

```` python
def linear_search(arr, target):
    """
    Tìm kiếm tuần tự: trả về chỉ số của target nếu tìm thấy, nếu không thì trả về -1.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Ví dụ sử dụng:
arr = [5, 3, 7, 1, 9, 4]
target = 7
index = linear_search(arr, target)
print("Tìm kiếm tuần tự: Phần tử", target, "tìm thấy ở vị trí:", index)
````
<hr>

# 2. Tìm kiếm nhị phân (Binary Search):
#### Yêu cầu dữ liệu phải được sắp xếp trước.
#### Ý tưởng: 
DCia danh sách ra làm đôi và so sánh phần tử giữa với giá trị cần tìm, sau đó lặp lại quá trình trên nửa danh sách thích hợp.
Ví dụ Python: Tìm kiếm nhị phân (Binary Search)
```` python
def binary_search(arr, target):
    """
    Tìm kiếm nhị phân: danh sách phải được sắp xếp.
    Trả về chỉ số của target nếu tìm thấy, nếu không thì trả về -1.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Ví dụ sử dụng:
arr_sorted = [1, 3, 4, 5, 7, 9]
target = 7
index = binary_search(arr_sorted, target)
print("Tìm kiếm nhị phân: Phần tử", target, "tìm thấy ở vị trí:", index)
````
<hr>

# VIII. Thuật toán sắp xếp
## 1. Sắp xếp chèn (Insertion Sort)
#### Ý tưởng:
Thuật toán sắp xếp chèn hoạt động bằng cách duyệt qua từng phần tử của danh sách và chèn mỗi phần tử đó vào vị trí thích hợp trong phần danh sách đã được sắp xếp trước đó. Quá trình này tiếp tục cho đến khi toàn bộ danh sách được sắp xếp.
Minh họa bằng Python:
```` python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Di chuyển các phần tử lớn hơn key về sau một vị trí
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ví dụ sử dụng:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Mảng sau khi sắp xếp chèn:", arr)
````
<hr>

## 2. Sắp xếp nổi bọt (Bubble Sort)
#### Ý tưởng:
Thuật toán sắp xếp nổi bọt hoạt động bằng cách liên tục duyệt qua danh sách, so sánh các cặp phần tử liền kề và hoán đổi chúng nếu chúng ở sai thứ tự. Quá trình này được lặp lại cho đến khi không còn cặp phần tử nào cần hoán đổi, tức là danh sách đã được sắp xếp.
Minh họa bằng Python:
```` python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Biến flag để kiểm tra xem có hoán đổi nào xảy ra không
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Hoán đổi nếu phần tử hiện tại lớn hơn phần tử kế tiếp
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Nếu không có hoán đổi nào xảy ra, danh sách đã được sắp xếp
        if not swapped:
            break

# Ví dụ sử dụng:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Mảng sau khi sắp xếp nổi bọt:", arr)
````
<hr>

## 3. So sánh hai thuật toán:

#### Độ phức tạp thời gian:

Cả hai thuật toán đều có độ phức tạp thời gian là O(n²) trong trường hợp xấu nhất và trung bình.

Trong trường hợp tốt nhất (danh sách đã được sắp xếp), sắp xếp chèn có độ phức tạp O(n), trong khi sắp xếp nổi bọt vẫn là O(n²).

#### Tính ổn định:

Cả hai thuật toán đều là thuật toán sắp xếp ổn định, tức là không thay đổi thứ tự tương đối của các phần tử có giá trị bằng nhau.

#### Ứng dụng:

Sắp xếp chèn hiệu quả hơn khi làm việc với các danh sách nhỏ hoặc danh sách gần như đã được sắp xếp.

Sắp xếp nổi bọt thường ít được sử dụng trong thực tế do hiệu suất kém hơn so với các thuật toán sắp xếp khác.
<hr>

# X. Tập hợp và ánh xạ
## 1. Tập hợp

<b>Khái niệm cơ bản</b>: Giới thiệu định nghĩa tập hợp, các phần tử của tập hợp và ký hiệu thuộc về (∈).

<b>Phân loại tập hợp</b>: Phân biệt tập hợp hữu hạn và vô hạn, tập hợp con, tập hợp bằng nhau, tập hợp rỗng (∅).

<b>Các phép toán trên tập hợp</b>: Giải thích các phép hợp (∪), giao (∩) và hiệu (–) của các tập hợp, cùng với các tính chất liên quan (như tính giao hoán, kết hợp và các quy tắc De Morgan).

#### Các phép toán trên tập hợp:
````python
# Khai báo các tập hợp A và B
A = {1, 2, 3}
B = {3, 4, 5}

# Phép hợp: A ∪ B
union = A.union(B)        # Hoặc dùng: A | B
print("Hợp của A và B:", union)  # Kết quả: {1, 2, 3, 4, 5}

# Phép giao: A ∩ B
intersection = A.intersection(B)  # Hoặc dùng: A & B
print("Giao của A và B:", intersection)  # Kết quả: {3}

# Phép hiệu: A - B
difference = A.difference(B)  # Hoặc dùng: A - B
print("Hiệu của A và B (A - B):", difference)  # Kết quả: {1, 2}

# Quy tắc De Morgan (ví dụ cho các tập hợp bổ sung)
# Giả sử U là tập hợp giao nhau của A và B, và A_complement là tập hợp phần tử không thuộc A trong U
U = {1, 2, 3, 4, 5, 6}
A_complement = U - A
B_complement = U - B
de_morgan_left = A_complement.intersection(B_complement)
de_morgan_right = U - (A.union(B))
print("De Morgan: (A ∪ B)^c =", de_morgan_right)
print("De Morgan: A^c ∩ B^c =", de_morgan_left)
````

## 2. Ánh xạ (Hàm số)

<b>Định nghĩa</b>: Một ánh xạ f từ tập A vào tập B là quy tắc gán mỗi phần tử của A cho duy nhất một phần tử của B (gọi là ảnh của phần tử đó).

<b>Tập nguồn và tập đích</b>: Phân biệt giữa tập nguồn (A) và tập đích (B), cũng như khái niệm tập xác định của ánh xạ và tập ảnh.

## 0. Các loại ánh xạ:

<b>Đơn ánh (Injective)</b>: Mỗi phần tử của A được gán cho một ảnh riêng biệt trong B.

<b>Toàn ánh (Surjective)</b>: Mỗi phần tử của B đều có ít nhất một tiền tố trong A.

<b>Song ánh (Bijective)</b>: Ánh xạ vừa đơn ánh vừa toàn ánh, cho phép tồn tại ánh xạ ngược.

#### Phép toán ánh xạ và hàm hợp:
```` python
# Định nghĩa hàm f và g
def f(x):
    return 2 * x + 1

def g(x):
    return x ** 2

# Hàm hợp g o f: (g o f)(x) = g(f(x))
def compose(f, g, x):
    return g(f(x))

# Thử nghiệm với một giá trị x
x_value = 3
result_f = f(x_value)              # f(3) = 2*3 + 1 = 7
result_g = g(result_f)             # g(7) = 7^2 = 49
result_compose = compose(f, g, x_value)

print("f({}) = {}".format(x_value, result_f))
print("g(f({})) = {}".format(x_value, result_g))
print("(g o f)({}) = {}".format(x_value, result_compose))
````
Sử dụng `map()` với hàm bình thường:
```` python
# Định nghĩa hàm bình phương
def square(x):
    return x * x

# Danh sách các số
numbers = [1, 2, 3, 4, 5]

# Áp dụng hàm square cho từng phần tử trong numbers
squared_numbers = map(square, numbers)

# Chuyển kết quả thành list và in ra
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
````
Sử dụng `map()` với hàm lambda
```` python
# Danh sách các số
numbers = [1, 2, 3, 4, 5]

# Áp dụng hàm lambda để bình phương từng phần tử
squared_numbers = map(lambda x: x * x, numbers)

# Chuyển kết quả thành list và in ra
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
````
Sử dụng `map()` với nhiều iterable:
```` python
# Hai danh sách số
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# Áp dụng hàm lambda để cộng từng cặp phần tử từ hai danh sách
sum_list = map(lambda x, y: x + y, list1, list2)

# Chuyển kết quả thành list và in ra
print(list(sum_list))  # Output: [11, 22, 33, 44]
````

#### Thao tác trên Dictionary
**Khởi tạo:**
- Bạn có thể khởi tạo một dictionary bằng cách sử dụng cặp dấu ngoặc nhọn `{}` hoặc hàm `dict()`.
```` python
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
````
Thêm hoặc Cập nhật phần tử:
- Thêm phần tử mới: Nếu khóa (key) chưa tồn tại trong dictionary, việc gán giá trị cho khóa đó sẽ thêm một cặp key-value mới.
- Cập nhật giá trị: Nếu khóa đã tồn tại, việc gán giá trị mới sẽ cập nhật giá trị hiện có.
````python
# Thêm phần tử mới
student['gpa'] = 3.8

# Cập nhật giá trị của key 'age'
student['age'] = 21

print(student)
# Output: {'name': 'An', 'age': 21, 'major': 'Computer Science', 'gpa': 3.8}
````
Truy xuất giá trị:
- Bạn có thể truy xuất giá trị của một key bằng cách sử dụng cú pháp `dictionary[key]` hoặc phương thức `get()`.
```` python
# Truy xuất giá trị bằng key
name = student['name']
print(name)  # Output: An

# Sử dụng phương thức get()
age = student.get('age')
print(age)  # Output: 21

# Truy xuất key không tồn tại bằng get() sẽ trả về None hoặc giá trị mặc định nếu được cung cấp
gpa = student.get('gpa', 'Chưa cập nhật')
print(gpa)  # Output: 3.8
````
Xóa phần tử:
- Sử dụng `del`: Xóa phần tử với key cụ thể.
- Sử dụng `pop()`: Xóa phần tử với key cụ thể và - trả về giá trị của phần tử đó.
- Sử dụng `popitem()`: Xóa và trả về cặp key-value cuối cùng trong dictionary.
- Sử dụng `clear()`: Xóa tất cả các phần tử trong dictionary.
```` python
# Truy xuất giá trị bằng key
name = student['name']
print(name)  # Output: An

# Sử dụng phương thức get()
age = student.get('age')
print(age)  # Output: 21

# Truy xuất key không tồn tại bằng get() sẽ trả về None hoặc giá trị mặc định nếu được cung cấp
gpa = student.get('gpa', 'Chưa cập nhật')
print(gpa)  # Output: 3.8
````