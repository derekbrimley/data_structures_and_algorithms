#!/usr/bin/env python3
from circular_linked_list import CircularLinkedList, CircularLinkedListIterator
from doubly_linked_list import DoublyLinkedList
from stack import Stack
from queue import Queue


class Processor(object):
    
    def __init__(self):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList()
        self.waiting = DoublyLinkedList()
        self.appetizers = Queue()
        self.buzzers = Stack()
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, f):
        '''Processes the given file stream.'''
        count = 0
        for line_i, line in enumerate(f):
            line = line.rstrip()
            # split and handle the commands here
            cmd = line.split(',')
            mth = cmd[0].lower()
            print("{}:{}".format(count,line))
            if mth == 'debug':
                self.debug()
            elif mth == 'song':
                print(self.songs_iter.next())
            elif mth == 'appetizer':
                cust = []
                for i in range(3):
                    cust.append(self.waiting.get(0))
                    self.waiting.delete(0)
                appetizer = self.appetizers.dequeue()
                print("{} >>> {}".format(appetizer, ', '.join([str(x) for x in cust])))
            elif mth == 'appetizer_ready':
                print(mth)
#            elif mth == 'call':
#                print(mth)
#            elif mth == 'arrive':
#                print(mth)
#            elif mth == 'seat':
#                print(mth)
#            elif mth == 'leave':
#                print(mth)
            
            count += 1

    def debug(self):
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()



#######################
###   Main loop

with open('example_data.csv') as f:
    processor = Processor()
    processor.run(f)

