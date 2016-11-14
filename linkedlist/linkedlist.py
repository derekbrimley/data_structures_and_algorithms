#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        current = self.head
        count = 0
        linked_list = []
        while current:
            linked_list.append(current.cargo)
            current = current.next
        print("{} >>> {}".format(self.size, ', '.join([str(x) for x in linked_list])))
    
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < 0 or index >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            current = self.head
            count = 0
            while current:
                if count == index:
                    return current
                current = current.next
                count += 1
            
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current:
                if current.next == None:
                    current.next = new_node
                    break
                current = current.next
        self.size += 1
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if index < 0 or index >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            new_node = Node(item)
            current = self.head
            count = 0
            while current:
                if index == 0:
                    new_node.next = current
                    self.head = new_node
                    break
                elif count == index - 1:
                    new_node.next = current.next
                    current.next = new_node
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
            new_node = Node(item)
            current = self.head
            count = 0
            while current:
                if index == 0:
                    new_node.next = current.next
                    self.head = new_node
                    break
                if count == index -  1:
                    new_node.next = current.next.next
                    current.next = new_node
                    break
                current = current.next
                count += 1
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < 0 or index >= self.size:
#            raise IndexError('Out of range')
            print('Error: {} is not within the bounds of the current list.'.format(index))
        else:
            current = self.head
            count = 0
            while current:
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
            current = self.head
            count = 0
            while current:
                if index == 0:
                    self.head = current.next
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
            node1 = self._get_node(index1)
            node2 = self._get_node(index2)

            node1.cargo, node2.cargo = node2.cargo, node1.cargo
            
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, cargo=None):
        self.cargo = cargo
        self.next = None
        
    def __str__(self):
        return str(self.cargo)