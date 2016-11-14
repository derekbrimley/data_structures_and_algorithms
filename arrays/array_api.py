#class ArrayMethod(object):
#    def __init__(self):
#        self.linked_list = LinkedList()
#        
#    def create(self, *args):
#        self.linked_list = LinkedList()
#        print('create')
#        
#    def debug(self, *args):
#        self.linked_list.debug_print()
#        
#    def add(self, *args):
#        print(args)
#        self.linked_list.add(args[0])
#        print(self.linked_list)
#        
#    def insert(self, *args):
#        print("insert")
#        
#    def set(self, *args):
#        print("set")
#    
#    def get(self, *args):
#        print("get")
#        
#    def delete(self, *args):
#        print("delete")
#        
#    def swap(self, **args):
#        print("swap")
#        
#with open('data_example.csv') as f:
#    for line in f:
#        line = line.rstrip('\n')
#        cmd = line.split(',')
#        args = (cmd[1], cmd[2])
#        a = ArrayMethod()
#        method = getattr(a, cmd[0].lower())
#        method(*args)

class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''
    
    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.array = alloc(initial_size)
        self.size = initial_size
        self.number = 0
        self.chunk_size = chunk_size
        
    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print("{} of {} >>> {}".format(self.number, self.size, ', '.join([str(x) for x in self.array])))
        
    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if 0 <= index + 1 <= self.number:
            return True
        else:
            return False
        
    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if self.number == self.size:
            self.size += self.chunk_size
            new_array = alloc(self.size)
            self.array = memcpy(new_array, self.array, self.size)
        
    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        
        if self.size >= self.number + self.chunk_size:
            self.size -= self.chunk_size
        
    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        self._check_increase()
        self.array[self.number] = item
        self.number += 1
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        if self._check_bounds(index):
            self._check_increase()
            for i, value in enumerate(self.array[index:self.number], start = index):
                self.array[index] = item
                self.array[i + 1] = value
            self.number += 1
        else:
            return self.out_of_range(index)
        
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            self.array[index] = item
        else:
            self.out_of_range(index)
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            print(self.array[index])
        else:
            return self.out_of_range(index)
    
    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            self.array[index] = None
            self.number -= 1
            
            for i, value in enumerate(self.array[index + 1:self.number + 1], start = index + 1):
                if i == self.size:
                    self.array[i] = None
                self.array[i - 1] = value
            print(self.size,self.number,self.array)
            self._check_decrease()
        else:
            self.out_of_range(index)
            
    
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if not self._check_bounds(index1):
            self.out_of_range(index1)
        elif not self._check_bounds(index2):
            self.out_of_range(index2)
        else:
            index1_value = self.array[index1]
            self.array[index1] = self.array[index2]
            self.array[index2] = index1_value
    
    def out_of_range(self, index):
        print('Error: {} is not within the bounds of the current array.'.format(index))

def alloc(size):
    new_array = [None] * size
    return new_array

def memcpy(dest, source, size):
    for index, value in enumerate(source):
        dest[index] = value
    return dest
