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

# Pool of words we will pick one at random later
word_list=['School','parkrun','python','coding','function','string','variable',
        'Hangman','monkey','necessary']
# Game title I used a little shell app called figlet to create it
# see how to create multiline strings with tripple '''
title='''
  _   _
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/
'''
def search_for_letter_in_word(word,letter,search_pointer=0,locations=[]):
    """ return a list containing all indexes of the letter in the word, the
    search_pointer and locations are used internally for the recursion to work 
    """
    search_pointer=word.find(letter,search_pointer)
    if (search_pointer==-1):
        return locations
    else:
        return search_for_letter_in_word(word,letter,search_pointer+1,
                locations+[search_pointer])

def replace_letter_in_word(word,letter,position):
    """ returns a new string which is word with the character at position
    replaced with letter
    """
    return word[:position] + letter + word[position+1:]

print(title) # Print our awesome title
lives=10 # Reset lives to 10
word=random.choice(word_list) # Picks a word at random from our word_list
word_lower=word.lower() # For checking let's use lowercase to avoid confusion
guess='_'*len(word) # Build up the guess blanks depending on length of the word
while True: # Infinte loop we will break if we win or lose
    print('')
    print(guess)
    print("You have {} guesses left".format(lives))
    # Get their letter change it to lower case just in case it's upper
    letter=input("Please type a letter: ").lower()
    # Find will return -1 if the letter isn't there so reduce the lives and
    # print a failure message
    if word_lower.find(letter)==-1:
        lives-=1
        print("Bad luck the word doesn't contain '"+letter+"'")
    else:
        # The letter must be there so get a list of locations of that letter
        locations=search_for_letter_in_word(word_lower,letter)
        # Loop through the list of locations and copy the letter at that
        # location in the original word to that location in the guess and print
        # a success message
        for loc in locations:
            guess=replace_letter_in_word(guess,word[loc],loc)
        print("Good guess the word did contain '"+letter+"'")
    # If live have run out break the loop and print failure message
    if lives<=0:
        print("Too bad you ran out of guesses, the word was "+word)
        break
    # If there are no blanks left break the loop and print success message
    if guess.find('_')==-1:
        print(guess)
        print("Well done, you guessed the word")
        break
print('')
print('Thanks for playing.')
