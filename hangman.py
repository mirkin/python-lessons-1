#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hangman Game

import random

try:
        input=raw_input
except NameError:
        pass
# Program starts from here, above is just to make it Python 2 and 3
# compatible

word_list=['School','parkrun','python','coding','function','string','variable',
        'Hangman','monkey','necessary']
title='''
  _   _
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/
'''

def search_for_letter_in_word(word,letter,searchPointer=0,locations=[]):
    searchPointer=word.find(letter,searchPointer)
    if (searchPointer==-1):
        return locations
    else:
        return search_for_letter_in_word(word,letter,searchPointer+1,
                locations+[searchPointer])

def replace_letter_in_word(word,letter,position):
    return word[:position] + letter + word[position+1:]

print(title)
lives=10
word=random.choice(word_list)
word_lower=word.lower()
guess='_'*len(word)
while True:
    print(guess)
    letter=input("Please type a letter: ").lower()
    if word_lower.find(letter)==-1:
        print("Bad luck the word doesn't contain '"+letter+"'")
    else:
        locations=search_for_letter_in_word(word_lower,letter)
        for loc in locations:
            guess=replace_letter_in_word(guess,word[loc],loc)
        print("Good guess the word did contain '"+letter+"'")
