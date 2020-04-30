
def binary_search(input_array,search_element):
    lower_index = 0
    upper_index = len(input_array) - 1
    
    while upper_index >= lower_index:
        middle_index = (upper_index + lower_index)//2
        if input_array[middle_index] == search_element:
            return middle_index
        elif input_array[middle_index] > search_element:
            upper_index = middle_index - 1
        elif input_array[middle_index] < search_element:
            lower_index = middle_index + 1
    return -1

input_array = [1,2,3,4]
search_element = 4
print(binary_search(input_array,search_element))

    
