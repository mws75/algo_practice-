my_list = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4 

def sort_list(my_list, target):
    sorted_list = []
    sorted_list.append(target)
    for i in range(len(my_list)):
        if my_list[i] != target:
            sorted_list.append(my_list[i])
    return sorted_list

def search_from_front(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            sorted_list = sort_list(my_list, target)
    return sorted_list 


new_list = search_from_front(my_list, target)
print(new_list)