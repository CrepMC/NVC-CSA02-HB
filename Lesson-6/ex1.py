# def linear_search(arr, nums):
#     for i in range(len(arr)):
#         if arr[i] == nums:
#             return i + 1
#     return -1



# print(linear_search([3, 6, 8, 9, 12], 8))



arr = [3, 6, 8, 9, 12, 100, 233, 11, 87], num = 8
arr_sort = [3, 6, 8, 9, 11, 12, 87, 100, 233], len = 5

def binary_search(arr, nums):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if arr[mid] == nums:
            return mid
        elif arr[mid] > nums:
            stop = mid - 1
        elif arr(mid) < nums:
            start = mid + 1
    return False

# Logarit: logb(x) = y, trong đó Logarit của x theo b là y sao cho b^y = x
# số lần tìm kiếm tối đa của mảng có len phần tử là : log2(len)