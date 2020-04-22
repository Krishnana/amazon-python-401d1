
# Method to get user input
def get_input():

    input_list = []
    try:
        n = int(input("Enter number of elements"))
        i = 1
        while i<=n:
            print(f"Enter number {i}")
            input_list.append(int(input())) 
            i = i + 1
        print(f"Input list {input_list}") 
    except: 
        print("Please enter only integers") 
    return input_list

# Method to reverse an array
def reverse_array_list(list):
    count = len(list)
    for i in range(count):
        first_item = list[i]
        if i < count/2:
            j = count - i - 1
            list[i] = list[j]
            list[j] = first_item
    print(f"Reverse Array is {list}")
    return list

print("Provide an array to reverse")
reverse_array_list(get_input())