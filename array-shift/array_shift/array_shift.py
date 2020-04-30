# Method to reverse an array
def insert_shift_array (list,val):
    """
    Description : This method will help to insert provided value to mid of index of input array
    Argument    : list --> input array with list of values
                  val --> value that will be inserted to mid of provided array
    return      : updated array with new value added at the middle index
    """
    
    new_array = [0] * (len(list)  + 1)
    count = len(new_array)
    for i in range(count):
        if i < count//2:
            new_array[i] = list[i]  
        elif i == count//2:
            new_array[i] = val
        else:
            new_array[i] = list[i -1]  
    return new_array

