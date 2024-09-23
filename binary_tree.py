my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
target = 13

def binary_search(my_list, target):
    found = False 
    current_list = []
    while found == False: 
        split_point = len(my_list) // 2
        if target == split_point: 
            return split_point