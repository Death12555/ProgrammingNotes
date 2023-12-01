def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

def binary_search(numbers_list, number_to_find):
    left_index= 0
    right_index= len(numbers_list) - 1
    mid_index= 0

    while left_index<= right_index:
        mid_index= (left_index + right_index) // 2
        mid_number= numbers_list[mid_index]

        if mid_number==number_to_find:
            return mid_index

        if mid_number<number_to_find:
            left_index= mid_index + 1
        else:
            right_index= mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index= (left_index + right_index)//2
    if mid_index>=len(numbers_list) or mid_index< 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number==number_to_find:
        return mid_index

    if mid_number<number_to_find:
        left_index= mid_index + 1
    else:
        right_index= mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)
    
def find_all_occurrences(lst, element):
    indices= []
    for index, value in enumerate(lst):
        if value==element:
            indices.append(index)
    return indices


if __name__ == '__main__':
    numbers_list= [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find= 21
    my_list = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2, 8]
    target_element = 2

    occurrences = find_all_occurrences(my_list, target_element)
    print(f"The element {target_element} is found at indices: {occurrences}")

    index= binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")