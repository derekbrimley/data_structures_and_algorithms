#!/usr/bin/env python3

class WordData(object):
    '''Data about a single word'''
    
    def __init__(self, book, word, count, percent):
        '''Constructor'''
        self.book = book
        self.word = word
        self.count = count
        self.percent = percent
        
    def __str__(self):
        return '{}, {}, {}, {}'.format(
            self.book, self.word, self.count, self.percent)
        