from statistics import mean, median, multimode

def calc_data(ls: list):
    mean_value = mean(ls)
    median_value = median(ls)
    multimode_value = multimode(ls)
    
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Multimode: {multimode_value}")
    
list1 = [1, 2 , 3, 3, 4, 4, 5]

calc_data(list1)