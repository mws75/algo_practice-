my_list = [1,2,3,4,5,6]
target = 3

def sort_list_transport(my_list, new_index, target): 
    sorted_list = []
    for i in range(len(my_list)):
        if i == new_index: 
            sorted_list.append(target)
            sorted_list.append(my_list[i])
        elif my_list[i] != target:
            sorted_list.append(my_list[i])
    return sorted_list

def sort_transportation(my_list, target): 
    sorted_list = []
    new_index = -1
    for i in range(len(my_list)):
        if my_list[i] == target: 
            new_index = i - 1 
            sorted_list = sort_list_transport(my_list, new_index, target)
    
    return sorted_list 

new_list = sort_transportation(my_list, target)
print(new_list)
