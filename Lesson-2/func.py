def calc_median(ls: list):
    ls.sort()
    print(ls)
    
    if (len(ls) % 2 == 1):
        mid = len(ls) // 2
        median = ls(mid)
    else:
        mid = len(ls) // 2 - 1
        median = ls[mid] + ls[mid + 1]
        median = median / 2
        
    return median

print(calc_median([3, 4, 6, 2, 4, 4, 2, 20 , 11, 9]))

