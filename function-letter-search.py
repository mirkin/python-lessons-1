#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program asks for a word and a letter. If the word contains one or more
# of those letters it will print the location of the letter(s) in the word.
# The index of the location starts at 0.
# We are introducing our own function to use.

try:
    input=raw_input
except NameError:
    pass
# Program starts from here, above is just to make it Python 2 and 3 compatible
def search_for_letter_in_word(word,letter):
    result_list=[]
    searchPointer=0
    while word.find(letter,searchPointer)!=-1:
        searchPointer=word.find(letter,searchPointer)
        result_list=result_list+[searchPointer]
        searchPointer=searchPointer+1
    return result_list

search_word=input('Type a word to search ')
target_letter=input('Type a letter to search ')
result=search_for_letter_in_word(search_word,target_letter)
print(result)
