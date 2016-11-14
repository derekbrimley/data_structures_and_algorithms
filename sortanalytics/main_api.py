#!/usr/bin/env python3
import time, copy, operator
from bubblesort import bubblesort
from insertionsort import insertionsort
from selectionsort import selectionsort
from quicksort import quicksort

FILENAMES = [
    [ 'list1.txt', 'int'   ], 
    [ 'list2.txt', 'int'   ], 
    [ 'list3.txt', 'int'   ], 
    [ 'list4.txt', 'int'   ], 
    [ 'list5.txt', 'float' ], 
    [ 'list6.txt', 'int'   ], 
]

SORTNAMES = [
    'nativesort',
    'bubblesort',
    'insertionsort',
    'selectionsort',
    'quicksort'
]

class Sorter(object):
    def bubblesort(self, list):
        bubblesort(list)

    def nativesort(self, list):
        sorted(list, key=float)

    def selectionsort(self, list):
        selectionsort(list)

    def insertionsort(self, list):
        insertionsort(list)

    def quicksort(self, list):
        quicksort(list)

class Result:
    def __init__(self, name, duration, nums):
        self.name = name
        self.duration = duration
        self.nums = nums
        self.relative = None

    def __str__(self):
        return '{}/{}'.format(self.name, self.duration)

def bubblesort_results(list, sorted_by_order):
    for i in range(0,len(list)):
        for j in range(0, i):
            sort_index = 0
            complete = False

            while not complete:

                current_attr = getattr(list[j], sorted_by_order[sort_index]['name'])
                next_attr = getattr(list[j+1],sorted_by_order[sort_index]['name'])

                if sorted_by_order[sort_index]['dir'] == 'asc':
                    order = operator.gt
                else:
                    order = operator.lt

                if order(current_attr, next_attr):
                    list[j], list[j+1] = list[j+1], list[j]

                elif operator.eq(current_attr, next_attr):
                    if sort_index < len(sorted_by_order) - 1:
                            sort_index += 1
                    else:
                        complete = True
                else:
                    complete = True
    return list

def main():
    files = []
    durations = {}
    results = []
    sorter = Sorter()
    for filename in FILENAMES:
        with open(filename[0], 'r') as f:
            file_nums = f.read().split()

        for sort in SORTNAMES:

            sort_method = getattr(sorter, sort)

            lists = []
            list_data = []
            for i in range(1000):
                list_data.append(file_nums)

            millis = time.time() * 1000.0

            for l in list_data:
                sort_method(l)

            duration = round((time.time() * 1000 - millis) / 1000, 6)

            nums = list_data[0]
            r = Result(sort, duration, nums)
            results.append(r)

        min_duration = 0
        for result in results:
            if min_duration == 0:
                min_duration = result.duration
            elif result.duration < min_duration:
                min_duration = result.duration

        relatives = []
        for result in results:
            result.relative = round(100.0 * (result.duration - min_duration) / min_duration, 6)
            relatives.append(result.relative)

        sorted_by_order = [
            {
                'name': 'duration',
                'dir': 'asc'
            }
        ]
        bubblesort_results(results, sorted_by_order)

        for result in results:
            print filename[0]
            print result.name
            print '{}%'.format(result.relative)
            print 'First 10: {}'.format(', '.join([x for x in result.nums[:10]]))
            print 'Last 10: {}'.format(', '.join([x for x in result.nums[-10:]]))
            print ''






### Main runner ###
if __name__ == '__main__':
    main()
