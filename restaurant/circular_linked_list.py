class Link:
    def __init__(self, data, next=None):
        self.cargo = data
        self.next = next
        
    def __str__(self):
        return str(self.cargo)
        
class CircularLinkedList(object):
    '''
     A circularly-linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        self.head = Link(None, None)
        self.head.next = self.head
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        current = self.head.next
        count = 0
        l = []
        while current.next != self.head:
            l.append(current)
            current = current.next
        l.append(current)
        print("{} >>> {}".format(self.size, ', '.join([str(x) for x in l])))
    
    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
        
        for i in range(count):
            self.debug_print()
            
    def _get_link(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < 0 or index >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            current = self.head.next
            count = 0
            while current != self.head:
                if count == index:
                    return current
                current = current.next
                count += 1
            
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        new_link = Link(item)
        current = self.head.next
        while current.next != self.head:
            current = current.next
        current.next = new_link
        new_link.next = self.head

        self.size += 1
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if index < 0 or index >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            new_link = Link(item)
            current = self.head.next
            count = 0
            while current.next != self.head:
                if index == 0:
                    new_link.next = current
                    self.head.next = new_link
                    break
                elif count == index - 1:
                    new_link.next = current.next
                    current.next = new_link
                    break
                current = current.next
                count += 1
            self.size += 1
            
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < 0 or index >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            new_link = Link(item)
            current = self.head.next
            count = 0
            while current.next != self.head:
                if index == 0:
                    new_link.next = current.next
                    self.head.next = new_link
                    break
                if count == index -  1:
                    new_link.next = current.next.next
                    current.next = new_link
                    break
                current = current.next
                count += 1
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < 0 or index >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            current = self.head.next
            count = 0
            while current != self.head:
                if count == index:
                    return current
                count += 1
                current = current.next
            
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if index < 0 or index  >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            current = self.head.next
            count = 0
            while current != self.head:
                if index == 0:
                    self.head.next = current.next
                    break
                elif count == index - 1:
                    current.next = current.next.next
                    break
                current = current.next
                count += 1
            self.size -= 1
                
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if index1 < 0 or index1 >= self.size:
#            raise IndexError('{} not within the bounds of the current list.'.format(index1))
            print('Error: {} is not within the bounds of the current list.'.format(index1))
        elif index2 < 0 or index2 >= self.size:
#            raise IndexError('{} not within the bounds of the current list.'.format(index2))
            print('Error: {} is not within the bounds of the current list.'.format(index2))
        else:
            link1 = self._get_link(index1)
            link2 = self._get_link(index2)

            link1.cargo, link2.cargo = link2.cargo, link1.cargo
        
        
######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    def __init__(self, circular_list):
        '''Starts the iterator on the given circular list.'''
        self.value = circular_list.head.next
        
    def has_next(self):
        '''Returns whether there is another value in the list.'''
        print('------------------------------------{}'.format(self.value))
        value = self.value
        if value == None:
            print('here')
            return False
        else:
            return True
        
    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
        next_value = self.value
        if self.value != None:
            self.value = self.value.next
        else:
            print('------------------------------')
            self.value = self.value.next.next
#            print('------------------------------')
        return next_value
    
    def __str__(self):
        return str(self.value)