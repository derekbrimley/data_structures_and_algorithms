import operator

def selectionsort(list, sorted_by_order):
    for filled in range(len(list) - 1, -1, -1):
        largest_spot = filled
        for index in range(0, filled):
            sort_index = 0
            complete = False
            
            while not complete:
                current_attr = getattr(list[index], sorted_by_order[sort_index]['name'])
                largest_attr = getattr(list[largest_spot],sorted_by_order[sort_index]['name'])

                if sorted_by_order[sort_index]['dir'] == 'asc':
                    order = operator.gt
                else:
                    order = operator.lt
                    
                if order(current_attr, largest_attr):
                    largest_spot = index
                    complete = True
                elif operator.eq(current_attr, largest_attr):
                    if sort_index < len(sorted_by_order) - 1:
                            sort_index += 1
                    else:
                        complete = True
                else:
                    complete = True
                    
        list[largest_spot], list[filled] = list[filled], list[largest_spot]
    return list