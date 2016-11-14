from bubblesort import bubblesort
from insertionsort import insertionsort
from selectionsort import selectionsort
from quicksort import quicksort

bubble_list     = [5,3,7,9,2,1,4,0,6,8]
insertion_list  = [5,3,7,9,2,1,4,0,6,8]
selection_list  = [5,3,7,9,2,1,4,0,6,8]
quicksort_list  = [5,3,7,9,2,1,4,0,6,8]

print("bubblesort:      {}".format(bubblesort(bubble_list)))
print("insertionsort:   {}".format(insertionsort(insertion_list)))
print("selectionsort:   {}".format(selectionsort(selection_list)))
quicksort(quicksort_list)
print("quicksort:       {}".format(quicksort_list))