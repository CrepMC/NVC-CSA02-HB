nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 9, 9, 20]
def has_duplicate(nums):
    return len(nums) != len(set(nums))

result = has_duplicate(nums)
print(result)