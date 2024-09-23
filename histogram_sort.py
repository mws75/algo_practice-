my_arr = [ 4,  3,  1,  7,  7,  8,  2,  9,  6,  5,  2,  5,  9,  2,  8,  3,  9,  4,  3,  1, 10,  6,  5,  4,  1,  5,  1,  8,  7,  2,  2,  1,  2,  1,  9,  6,  2,  2,  2,  3,  7,  7,  2,  9,  7,  9,  3,  8,  7,  6]


def histogram_sort(arr, max_value):
    
    histogram = [0] * max_value
    
    for i in range(len(arr)):
        histogram[arr[i] - 1] += 1 
        
    return histogram


def most_frequent(histogram):
    most_frequent = 0 
    for i in range(len(histogram)):
        if histogram[i] > histogram[most_frequent]: 
            most_frequent = i
    return most_frequent + 1 # because we need to add one since we started at 0

    

histogram = histogram_sort(my_arr, 10)
print(histogram)
most_frequent_value = most_frequent(histogram)
print(f"the most frequent value is: {most_frequent_value}")

