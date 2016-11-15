#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hangman Game little more sophisticated than the basic version

import random

try:
        input=raw_input
except NameError:
        pass
# Program starts from here, above is just to make it Python 2 and 3
# compatible

# Pool of words we will pick one at random later
word_list=['School','parkrun','python','coding','function','string','variable',
        'Hangman','monkey','necessary','toad in the hole','thick and thin',
        'flip-flops']
blank_character='_'
word_seperator=' '
screen_width=80
# Game title I used a little shell app called figlet to create it
# see how to create multiline strings with tripple '''
title='''
  _   _
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/ Version: 2.0
'''
# Message to show when a user quits the application
bye_message='''
 ________             __          ____           ___  __          _          
/_  __/ /  ___ ____  / /__ ___   / __/__  ____  / _ \/ /__ ___ __(_)__  ___ _
 / / / _ \/ _ `/ _ \/  '_/(_-<  / _// _ \/ __/ / ___/ / _ `/ // / / _ \/ _ `/
/_/ /_//_/\_,_/_//_/_/\_\/___/ /_/  \___/_/   /_/  /_/\_,_/\_, /_/_//_/\_, / 
                                                          /___/       /___/  

   ____                        ____                        __  __  __     
  /\  _`\                     /\  _`\                     /\ \/\ \/\ \    
  \ \ \L\ \  __  __     __    \ \ \L\ \  __  __     __    \ \ \ \ \ \ \   
   \ \  _ <'/\ \/\ \  /'__`\   \ \  _ <'/\ \/\ \  /'__`\   \ \ \ \ \ \ \  
    \ \ \L\ \ \ \_\ \/\  __/    \ \ \L\ \ \ \_\ \/\  __/    \ \_\ \_\ \_\ 
     \ \____/\/`____ \ \____\    \ \____/\/`____ \ \____\    \/\_\/\_\/\_\\
      \/___/  `/___/> \/____/     \/___/  `/___/> \/____/     \/_/\/_/\/_/
                 /\___/                      /\___/                       
                 \/__/                       \/__/                        
'''
# Fill array with 10 blank strings then fill with ASCII art for each stage
visual_lives=['']*10

visual_lives[0]='''
   +---------+
   |         |
   @         |
  /H\        |
  / \        |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[1]='''
   +---------+
   |         |
   @         |
  /H\        |
    \        |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[2]='''
   +---------+
   |         |
   @         |
  /H         |
    \        |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[3]='''
   +---------+
   |         |
   @         |
  /H         |
             |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[4]='''
   +---------+
   |         |
   @         |
  /          |
             |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[5]='''
   +---------+
   |         |
   @         |
             |
             |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[6]='''
   +---------+
   |         |
             |
             |
             |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[7]='''
   +---------+
             |
             |
             |
             |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[8]='''
             |
             |
             |
             |
  ___________|___________
 /           |          /|
/______________________/ |
|                      | /
|______________________|/
'''
visual_lives[9]='''
  _______________________
 /                      /|
/______________________/ |
|                      | /
|______________________|/
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

def validate_letter(letter,show_error_message=True):
    """ check letter is a single letter
    """
    if len(letter)!=1:
        print_center_text('Whoops you need to type a single letter')
        return False
    if not letter.isalpha():
        print_center_text('I can only accept letters')
        return False
    return True

def map_char_from_word1_to_word2(word1,word2,search_char,replace_char):
    """ seach word1 for all occurences a character and at those locations in
    word2 replace the characters with the replacement character.
    map_char_from_word1_to_word2('school','******','o','!') would return
    '***!!*'
    """
    locations=search_for_letter_in_word(word1,search_char)
    for loc in locations:
        word2=replace_letter_in_word(word2,replace_char,loc)
    return word2

def yes_or_no(question=''):
    """ allow user to type yes/no YES/NO y/n Y/N to a given question and
    return True if they type yes False for no. It will deal with cases where
    they don't type in something sensible
    """
    answered=False
    while not answered:
        if question!='':
          print_center_text (question)
        answer=input().lower()
        if answer!='yes' and answer!='no' and answer!='y' and answer!='n':
          print_center_text ("Sorry, I don't understand '"+answer+
            "' please answer yes or no or y or n.")
        else:
          answered=True
    if answer=='n' or answer=='no':
        return False
    return True

def print_center_text(text):
    lines=text.split('\n')
    max_length=0
    for line in lines:
        if len(line)>max_length:
            max_length=len(line)
    padding=" "*((80-max_length)/2)
    for line in lines:
        print(padding+line)

def play_game():
    """ Play a round of hangman
    """
    print_center_text(title) # Print our awesome title
    lives=9 # Reset lives
    incorrect_guesses=[] # list to hold mistakes
    correct_guesses=[] # list to hold valid guesses
    word=random.choice(word_list) # Picks a word at random from our word_list
    # For checking let's use lowercase to avoid confusion
    word_lower=word.lower()
    # Build up the guess blanks depending on length of the word
    guess=blank_character*len(word)
    # Show spaces in the guess
    guess=map_char_from_word1_to_word2(word_lower,guess,' ',word_seperator)
    # Show any dashes in guess
    guess=map_char_from_word1_to_word2(word_lower,guess,'-','-')
    while True: # Infinte loop we will break if we win or lose
        print_center_text(visual_lives[lives])
        print_center_text('')
        print_center_text(guess)
        print_center_text("You have {} guesses left".format(lives))
        if len(incorrect_guesses)>0:
            print_center_text("Incorrect guesses: "+",".join(incorrect_guesses))
        if len(correct_guesses)>0:
            print_center_text("Correct guesses: "+",".join(correct_guesses))
        # Continually request a letter change it to lower case just in case it's
        # upper. Only move on if it's a valid guess
        while True:
            letter=input("Please type a letter: ").lower()
            if validate_letter(letter):
                break
        # Find will return -1 if the letter isn't there so reduce the lives and
        # print a failure message. Also add letter to bad guesses
        if word_lower.find(letter)==-1:
            lives-=1
            incorrect_guesses.append(letter)
            print_center_text("Bad luck the word doesn't contain '"+letter+"'")
        else:
            # Correct guess so add it to the list
            correct_guesses.append(letter)
            # The letter must be there so get a list of locations of that letter
            locations=search_for_letter_in_word(word_lower,letter)
            # Loop through the list of locations and copy the letter at that
            # location in the original word to that location in the guess and
            # print a success message
            for loc in locations:
                guess=replace_letter_in_word(guess,word[loc],loc)
            print_center_text("Good guess the word did contain '"+letter+"'")
        # If live have run out break the loop and print failure message
        if lives<=0:
            print_center_text(visual_lives[0])
            print_center_text("Too bad you ran out of guesses, the word was "+word)
            break
        # If there are no blanks left break the loop and print success message
        if guess.find(blank_character)==-1:
            print_center_text(guess)
            print_center_text("Well done, you guessed the word")
            break
    print('')
    print_center_text('Thanks for playing.')

while True:
    play_game()
    if not yes_or_no('Play again? (y/n)'):
        break

print_center_text(bye_message)
