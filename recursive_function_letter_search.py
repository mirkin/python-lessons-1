#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Same as function-letter-search.py we find all the letters in a word or
# sentence, but using recursion.

try:
        input=raw_input
except NameError:
        pass
# Program starts from here, above is just to make it Python 2 and 3
# compatible
def search_for_letter_in_word(word,letter,searchPointer=0,locations=[]):
    searchPointer=word.find(letter,searchPointer)
    if (searchPointer==-1):
        return locations
    else:
        return search_for_letter_in_word(word,letter,searchPointer+1,
                locations+[searchPointer])

target=raw_input('Type a word to search ')
searchLetter=raw_input('Type a letter to search ')
locations=search_for_letter_in_word(target,searchLetter)
print locations
