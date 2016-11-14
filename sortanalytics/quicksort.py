def quicksort(quicksort_list):
    quicksort_helper(quicksort_list, 0, len(quicksort_list)-1)
    
def quicksort_helper(quicksort_list, first, last):
    if first < last:
        part = partition(quicksort_list, first, last)
        
        quicksort_helper(quicksort_list, first, part-1)
        quicksort_helper(quicksort_list, part+1, last)

def partition(quicksort_list, first, last):
    pivot = quicksort_list[first]
    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and quicksort_list[left] <= pivot:
            left = left + 1
        while quicksort_list[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = quicksort_list[left]
            quicksort_list[left] = quicksort_list[right]
            quicksort_list[right] = temp

    temp = quicksort_list[first]
    quicksort_list[first] = quicksort_list[right]
    quicksort_list[right] = temp

    return right