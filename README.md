#Python Lessons \#1 
Python/Coding lessons for my kids public for anyone else who may want to learn

**Program Examples**

* [Our first program](#our-first-program)
* [Letter in word search](#letter-in-word-search)
* [Letter in word search function](#letter-in-word-search-function)
* [Letter in word search recursive function]
(#letter-in-word-search-recursive-function)


##Intro

Our physical computing projects (robots, LEDs, etc.) are a great way to dive
straight into something exciting and get hacking. We back those projects up
with these lessons which give a deeper understanding of programming.

We don't boot into a desktop environment, we use the shell and edit the files
using vim. This isn't for everyone, you can use any text editor such as atom or
sublime or even a web browser on a site such as
[https://repl.it/languages/python3](https://repl.it/languages/python3) which is
a great way to be up and running immediately.

We run the program from a terminal/shell by typing one of the 5 following
commands.

```bash
python hello-world.py
python3 hello-world.py
ipython hello-world.py
ipython3 hello-world.py
hello-world.py
```
The first 2 should work for most systems, the difference being the version of
python used. The ipython would require you to have ipython installed, and the
last method would require your file to be executable.

You may also be able to run it from a desktop by launching the file. This will
often open the file in a program called IDLE and you can run by selecting run
module from the menu.

## Our first program

Code [hello-world.py](hello-world.py)

The traditional first program simply prints Hello World to the screen. Our
program is stored in a file name with .py at the end which is the python file
extension. This helps users and systems to associate the file with python.

The code below you can ignore. The first line is for your operating system to
tell it what program to use to run this file. The second line allows us to
write unicode in our strings.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

Next we are calling a function with a string literal. A function has a name in
this case **print** to call a function you use it's name followed by () you can
send functions information inside the parentheses. The print function prints
whatever you send it to the screen. We are sending it a string which is a
sequence of characters. In python we can make a string by putting our
characters inside '' in this case print('Hello World') 

### Letter in word search

Code [letter-search.py](letter-search.py)

User types in a word and a letter, the letter is searched for in the word and
the locations of that letter are printed to the screen.

Here we use a while loop, and the find method which is available for python
strings.


### Letter in word search function

Code [function-letter-search.py](function-letter-search.py)

This is the same as letter in word search but we define our own function.
Instead of printing the index of each letter found we return a list of indexes.
Using our own function allows us to repeat functionality again and again
without having to write extra code. We simply call the function.  
Unless we need to modify the function we can forget how it works and anyone
wishing to use it doesn't need to know how it works to use it. We just need to
know what it does, what we need to send it and what it will return.

### Letter in word search recursive function

Code [recursive-function-letter-search.py](recursive-function-letter-search.py)

Here we write the same function as  we did in the past, but we use recursion.
Run the code in your head or on paper to see how it works. Feel free to skip
recursion and come back later when you are interesed in learning about
recursion.  
Keep in mind every time the function is called it has it's own scope. Another
copy of it's local variables.
