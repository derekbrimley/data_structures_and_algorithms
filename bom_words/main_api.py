#!/usr/bin/env python3
import random, re
from worddata import WordData
from merge_api import merge_lists
from bubblesort import bubblesort
from insertionsort import insertionsort
from selectionsort import selectionsort

FILENAMES = [
    [ '1 Nephi',         '01-1 Nephi.txt' ],
    [ '2 Nephi',         '02-2 Nephi.txt' ],
    # [ 'Jacob',           '03-Jacob.txt' ],
    # [ 'Enos',            '04-Enos.txt' ],
    # [ 'Jarom',           '05-Jarom.txt' ],
    # [ 'Omni',            '06-Omni.txt' ],
    # [ 'Words of Mormon', '07-Words of Mormon.txt' ],
    # [ 'Mosiah',          '08-Mosiah.txt' ],
    # [ 'Alma',            '09-Alma.txt' ],
    # [ 'Helaman',         '10-Helaman.txt' ],
    # [ '3 Nephi',         '11-3 Nephi.txt' ],
    # [ '4 Nephi',         '12-4 Nephi.txt' ],
    # [ 'Mormon',          '13-Mormon.txt' ],
    # [ 'Ether',           '14-Ether.txt' ],
    # [ 'Moroni',          '15-Moroni.txt' ],
]

###################################
###   Analyze a string of words

def analyze_text(book, text):
    '''Performs a very naive analysis of the words in the text, returning the SORTED list of WordData items'''
    # lowercase the entire text
    text = text.lower()
    # split the text by whitespace to get a list of words
    words = text.split()
    # convert each word to the longest run of characters
    # eliminate any words that are empty after conversion to characters
    wordcounts = {}
    total = len(words)

    for i, word in enumerate(words):
        m = re.match(r'(?P<word>[a-z]+)', word)
        if m:
            words[i] = m.group('word')
        else:
            words.remove(word)

    for word in words:
        wordcounts[word] = wordcounts.get(word, 0) + 1

    worddata = []

    for key, value in wordcounts.items():
        percent = round(((value * 1.0) / total) * 100, 1)
        wd = WordData(book, key, value, percent)
        worddata.append(wd)

    sort_by_order = [
        {'name': 'percent', 'dir': 'desc'},
        {'name': 'count', 'dir': 'desc'},
        {'name': 'word', 'dir': 'asc'}
    ]

    r = random.randint(0,2)
    if r == 0:
        worddata = bubblesort(worddata, sort_by_order)
    elif r == 1:
        worddata = insertionsort(worddata, sort_by_order)
    else:
        worddata = selectionsort(worddata, sort_by_order)

    return worddata
    # sort the WordData list using Bubble Sort, Insertion Sort, or Selection Sort:
    # 1. highest percentage [descending]
    # 2. highest count (if percentages are equal) [descending]
    # 3. lowest alpha order (if percentages and count are equal) [ascending]

    # return


################################
###   Prints a words list

def print_words(words, **kwargs):
    '''Prints a list of words'''
    # print the words over the threshold_percent or that match the given word

    if 'threshold' in kwargs:
        for word in words:
            if getattr(word, 'percent') > kwargs['threshold']:
                print(word)

    if 'word' in kwargs:
        for word in words:
            if getattr(word, 'word') == kwargs['word']:
                print(word)
    # print an empty line
    print('')


#######################
###   Main loop

def main():
    '''Main program'''
    master = []
    threshold = 2.0
    # loop through the filenames and analyze each one

    # after analyzing each file, merge the master and words lists into a single, sorted list (which becomes the new master list)
    print('INDIVIDUAL BOOKS > 2%')
    for filename in FILENAMES:
        with open(filename[1], 'r') as f:
            text = f.read()

            analyzed_text = analyze_text(filename[0],text)

        print_words(analyzed_text, threshold=threshold)
#        print 'master: ', master
        master = merge_lists(master, analyzed_text)

#    for word in master:
#        print word.book
    # print each book, word, count, percent in master list with percent over 2
    print('MASTER LIST > 2%')
    print_words(master, threshold=threshold)

    # print each book, word, count, percent in master list with word == 'christ'
    print('MASTER LIST == christ')
    print_words(master, word='christ')

    # read the full text of the BoM and analyze it
    print('FULL TEXT > 2%')

    full_text = ''
    for filename in FILENAMES:
        with open(filename[1], 'r') as f:
            text = f.read()
            full_text += text

    full_text_analyzed = analyze_text('Book of Mormon', full_text)
    print_words(full_text_analyzed, threshold=threshold)

#######################
###   Runner

if __name__ == '__main__':
    main()
