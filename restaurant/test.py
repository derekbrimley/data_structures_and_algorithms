#!/usr/bin/env python3
#from queue import Queue
#
#ll = Queue()
#ll.enqueue('a')
#ll.enqueue('b')
#ll.enqueue('c')
#ll.debug_print()
#print(ll.dequeue())
#ll.enqueue('d')
#ll.debug_print()
#print(ll.dequeue())
#print(ll.dequeue())
#ll.debug_print()
#print(ll.size)

#from circular_linked_list import CircularLinkedList
#
#cll = CircularLinkedList()
#cll.add(1)
#cll.add(2)
#cll.add(3)
#cll.add(4)
#cll.add(5)
#cll.insert(4,10)
#cll.set(0,'what')
#print('0: {}'.format(cll.get(0)))
#print('1: {}'.format(cll.get(1)))
#print('2: {}'.format(cll.get(2)))
#print('3: {}'.format(cll.get(3)))
#print('4: {}'.format(cll.get(4)))
#print('5: {}'.format(cll.get(5)))
#cll.delete(5)
#cll.swap(1,3)
#cll.swap(0,2)
#cll.debug_print()
#cll.debug_cycle(2)

#from doubly_linked_list import DoublyLinkedList
#
#dll = DoublyLinkedList()
#dll.add(1)
#dll.add(2)
#dll.add(3)
#dll.add(4)
#dll.add(5)
#dll.insert(4,10)
#dll.set(0,'what')
#print('0: {}'.format(dll.get(0)))
#print('1: {}'.format(dll.get(1)))
#print('2: {}'.format(dll.get(2)))
#print('3: {}'.format(dll.get(3)))
#print('4: {}'.format(dll.get(4)))
#print('5: {}'.format(dll.get(5)))
#dll.delete(5)
#dll.swap(1,3)
#dll.swap(0,2)
#dll.debug_print()

#from stack import Stack
#
#s = Stack()
#s.push(1)
#s.push(2)
#s.push(3)
#s.push(4)
#s.push(5)
#s.push(6)
#s.push(7)
#s.push(8)
#s.pop()
#s.pop()
#s.pop()
#s.pop()
#s.debug_print()

from queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.size())
q.debug_print()