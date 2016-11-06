#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program asks for a word and a letter. If the word contains one or more
# of those letters it will print the location of the letter(s) in the word.
# The index of the location starts at 0.

try:
    input=raw_input
except NameError:
    pass
# Program starts from here, above is just to make it Python 2 and 3 compatible
target=input('Type a word to search ')
searchLetter=input('Type a letter to search ')
searchPointer=0
while target.find(searchLetter,searchPointer)!=-1:
    searchPointer=target.find(searchLetter,searchPointer)
    print(str(searchPointer))
    searchPointer=searchPointer+1
