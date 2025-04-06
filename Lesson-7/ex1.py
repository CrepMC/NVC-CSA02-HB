import time

# Insertion Sort
arr = [1, 10, 13, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
start_time = time.time()
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
end_time = time.time()
print(f"Insertion Sort Time: {end_time - start_time} seconds")

# Bubble Sort
arr = [1, 10, 13, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
n = len(arr)
start_time = time.time()
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
end_time = time.time()
print(f"Bubble Sort Time: {end_time - start_time} seconds")
