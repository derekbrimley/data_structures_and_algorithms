import operator 

def insertionsort(list, sorted_by_order):
    for i in range(1,len(list)):
        current = list[i]
        
        while i > 0:
            sort_index = 0
            complete = False
            
            while not complete:
                insert_attr = getattr(list[i], sorted_by_order[sort_index]['name'])
                prev_attr = getattr(list[i-1],sorted_by_order[sort_index]['name'])

                if sorted_by_order[sort_index]['dir'] == 'desc':
                    order = operator.gt
                else:
                    order = operator.lt

                if order(insert_attr,prev_attr):
                    list[i], list[i-1] = list[i-1], list[i]
                    
                elif operator.eq(insert_attr, prev_attr):
                    if sort_index < len(sorted_by_order) - 1:
                            sort_index += 1
                    else:
                        complete = True
                else:
                    complete = True

            i -= 1
        
    return list