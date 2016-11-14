def insertionsort(list):
    for i in range(1,len(list)):
        current = list[i]
        
        while i > 0:
            if list[i] < list[i - 1]:
                list[i], list[i - 1] =  list[i - 1], list[i]
            i -= 1
        
    return list