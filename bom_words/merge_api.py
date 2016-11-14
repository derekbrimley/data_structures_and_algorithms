#!/usr/bin/env python3

def merge_lists(listA, listB):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''
    
    sorts = ['percent', 'count', 'word']
    merged_list = []
    
    if not len(listA) or not len(listB):
        return listA + listB
    
    val_a = listA.pop(0)
    val_b = listB.pop(0)
    
    complete = False
    index = 0
    while not complete:
        a_attr = getattr(val_a, sorts[index])
        b_attr = getattr(val_b, sorts[index])
        
        if a_attr > b_attr:
            index = 0
            merged_list.append(val_a)
            try:
                val_a = listA.pop(0)
            except IndexError:
                merged_list.extend(listB)
                complete = True
                
        elif a_attr < b_attr:
            index = 0
            merged_list.append(val_b)
            try:
                val_b = listB.pop(0)
            except IndexError:
                merged_list.extend(listA)
                complete = True
        else:
            if index < len(sorts) - 1:
                index += 1
            else:
                index = 0

                merged_list.append(val_a)
                try:
                    val_a = listA.pop(0)
                except IndexError:
                    merged_list.extend(listA)
                    complete = True

    return merged_list