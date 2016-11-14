def selectionsort(list):
    for filled in range(len(list) - 1, -1, -1):
        largest_spot = filled
        for index in range(0, filled):
            if list[index] > list[largest_spot]:
                largest_spot = index
        list[largest_spot], list[filled] = list[filled], list[largest_spot]
    return list