##################################
####BUBBLE SORT


def bubble_sort(list):
    for i in range(0,len(list)):
        for j in range(0, i):
            if list[i] < list[j]:
                list[j], list[i] = list[i], list[j]
    return list

def insertion_sort(list):
    for i in range(1,len(list)):
        current = list[i]
        index = i
        
        while index > 0 and list[index - 1] > current:
            list[index] = list[index - 1]
            index = index - 1
        
        list[index] = current
    return list

def selection_sort(list):
    for filled in range(len(list) - 1, 0, -1):
        largest_spot = 0
        for index in range(1, filled + 1):
            if list[index] > list[largest_spot]:
                largest_spot = index
        list[largest_spot], list[filled] = list[filled], list[largest_spot]
    return list


bubble_list = [5,3,7,9,2,1,4,0,6,8]
insertion_list = [5,3,7,9,2,1,4,0,6,8]
selection_list = [43,76,123,45,3,987,54]
print(bubble_sort(bubble_list))
print(insertion_sort(insertion_list))
print(selection_sort(selection_list))