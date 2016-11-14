import operator

def bubblesort(list, sorted_by_order):
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