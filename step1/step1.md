# First ever Python code

Use trinket to open a new project - this will be your first Python code, so give your project a name to show this.

The trinket window has two parts - to the left is the *coding panel* where you write your code; to the right is the *results panel* where the output of your code appears.

In Python code a lot of the words you type are followed by brackets: ```()``` and sometimes there are things typed inside the brackets, and sometimes they are empty. When a word in Python is followed by brackets it means it is a Python ***function*** which means it carries out some action for us. At first we will use functions written by someone else, but later we will write our own functions.

## print()

The first function to use is the Python ```print()``` function, which causes something to be printed in the results panel.

Make sure the first line of your project has this code:

``` python
#!/bin/python3
```

then, in the next line, type

``` python
print('Hello')
```

(Make sure you include the quote marks around the word Hello.)

Click on the triangle labelled **Run** and see what happens.

Now change the single quote marks ```'``` to double quote marks ```"``` and see what happens.

When we put letters and/or numbers inside quote marks Python calls this a *text string*. A text string is a type of Python *object*. Python lets you use single quotes or double quotes to make a text string.

Many Python functions let you put more than one thing inside the brackets, and in this case you have to separate the different items with a comma ```,```. Try

``` python
print('Taylor', 'Swift')
```

You will see it prints one text string after the other (and also puts a space between the items).

We can also use ```print()``` to print numbers.

``` python
print(5)
```

Numbers are a different type of Python object - you can do some things with numbers that you can't do with text strings, and vice versa.

### Python arithmetic

Python can do arithmetic with numbers using the signs

- \+ for addition
- \- for subtraction
- \* for multiplication and
- \/ for division.

You can work out a sum inside the brackets in a ```print()``` function.

Try these lines of code:

```python
print(4 + 2)
print(4 - 2)
print(4 * 2)
print(4 / 2)
```

Click on **Run** to try out your code.

You might notice that the last sum  - the division sum - prints the answer slightly differently to the others as it prints a decimal point and a zero after the answer.

Python has different types of number objects and the two main types are whole numbers, called *integers*, which don't have any decimal values, and decimal numbers, called *floating point numbers* which have a decimal point, and numbers after it. When Python does a division sum it *always* gives the answer as a decimal number, not a whole number.

You can do some things with integers that you can't do with decimal numbers, and vice versa.

## The Interactive Python Console

Open a new tab in your browser and go to this link:

[trinket.io/console](https://trinket.io/console)

This opens the Interactive Python Console, where the left end of each line begins with three *greater than* signs: ```>>>```.

You can use the console to try out Python code. It's really handy, because you can get it to show the result of your code without having to keep using the ```print()``` function.

In the console type:

``` python
2 + 4
```

and press Return. The console gives you the answer straight away.

You can combine different arithmetic operations.

In the console type

``` python
2 + 3 * 4
```

and try to predict the answer before you press Return.

Did you get it right?

<details><summary>Click here if you didn't</summary>

<p></p>
If you thought the answer would be 20 you may have forgotten the rule BODMAS which tells you that you have to do multiplication <i>before</i> addition.
<p></p>
How could you add a left and a right bracket to the sum so that the answer <i>would</i> be 20?
<p></p>
  
</details>

### Arithmetic with text strings

You can also do arithmetic with text strings. You can use + to add text strings together:

``` python
'Good' + 'morning'
```

but did you notice Python *didn't* put a space between the words this time?

You can multiply a text string by a number to repeat it. Here we make the computer laugh:

``` python
'Ha' * 10
```

Here is a little Python exercise to do with addition, and it involves numbers and text strings. Type this into the interactive console but before you press Return try to predict what output it will give:

``` python
20 + 24
```

Now try this

``` python
"20" + "24"
```

Now this

``` python
"20 + 24"
```

Now this

``` python
"20" + 24
```

The last one gives an error because we are accidentally mixing different types of objects in the addition sum: ```"20"``` is a text string and ```24``` is a number. You can add together objects of the *same* type but you can't mix types in an addition sum.

In the next step we will come across special functions which can change Python objects from one type to another.

## Python comments

Go back to your trinket project with your first ever Python code.

Every time you run the code it will carry out all the instructions from the top. As you add extra code to the end of your project you may want Python to ignore some of the earlier lines of code to avoid cluttering up the output.

To make Python ignore a line of code place the ```#``` character in the left hand column - this turns that line of code into a *comment*, which is skipped over by Python.

In fact *comments* are extremely useful because you can use them to make notes in the middle of your code about what each bit of code is doing. As you write more complicated code comments can save you a lot of time in helping you find the right bit of your code which might need editing.

For example, you could put this comment line above the lines of code where you used the addition, subtraction, multiplication and division operators:

```python
# Demonstration of Python arithmetic
```

## Python libraries

When you start a new Python project you have lots of basic Python functions available to use and these will allow you to do a lot of coding. This is like a pizza base with just the basic ingredients.

Sometimes you want to do other tasks which are not included in the basic Python functions, and for this there are a huge number of Python ***libraries*** containing extra functions which you can use. These are like the extra toppings on your pizza.

To use functions from a library you have to ***import*** the library, and ```import``` instructions should go at the top of your project immediately after the ```#!/bin/python3``` line.

One library we often use is the ```random``` library, which contains a lot of functions which use random numbers, so this is often used in games.

To import **all** the functions in the ```random``` library you would use the code:

``` python
from random import *
```

Sometimes you only want to import *one* function from a library. If you only wanted to import the ```randint``` function from the ```random``` library (which generates random integers) you would use

``` python
from random import randint
```

The ```randint()``` function generates random integers - put two numbers inside the brackets to show the smallest and largest numbers you want to generate.

``` python
randint(1,10)
```

will generate a random integer between 1 and 10.

Another useful library is the ```time``` library, which has functions involving dates, times and a function called ```sleep``` to make the code wait for a length of time.

To import the ```sleep``` function from the ```time``` library you would use

``` python
from time import sleep
```

Once you've imported the ```sleep``` function you can use it in your code. For example, this code would make the Python code *wait* for 5 seconds:

``` python
sleep(5)
```

But if you *haven't* imported the sleep function then your code would give an error.

We can practise using imported functions in your code. Make sure you have imported the two functions randint and sleep:

``` python
from random import randint
from time import sleep
```

then type in this code:

``` python
sleep(randint(2,7))
print('BOO!')
```

Here we've used ```randint(2,7)``` to generate a random integer between 2 and 7, and then we've used this random number in the ```sleep()``` function so we will wait for a random number of seconds.

It's very common in Python to put one function *inside* another.

## Python variables

In Scratch you can create a lot of projects without ever using variables, but in Python you will find you need to use variables in virtually every project.

A variable is like a *label* stuck on a storage box in the computer's internal memory - which consists of millions of storage boxes. Inside the box you can place any of the different types of Python objects - numbers, text strings, turtles (yes, really!) etc.

Python uses the sign ```=``` to make a variable. To the left of the ```=``` sign you put the *name* of the variable, and to the right you put the object that you want the variable to point to. The Python code

``` python
a = 5
```

puts the number object ```5``` in a storage box, and puts the label ```a``` on the box.

The code

``` python
myname = "Hagrid"
```

puts the text string object ```"Hagrid"``` in a storage box, and puts the label ```myname``` on the box.

**Note:** In Python the ```=``` sign has a slightly different meaning from the way it's used in maths. In maths it indicates two things which are equal to each other; in Python it means you take a Python object, which is on the *right* of the = sign, and give it a label (variable name), which is on the *left* of the = sign.

### Variable names

You can use any letter of the alphabet, capital or small, in your variable names, and the numbers 0 to 9 and the underscore ```_``` character, BUT the first character of the variable name *can't* be a number.

There are some words you should avoid for variable names, as these are Python *key words* used in other Python commands - these are

```and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield```

Be careful!! Python is very fussy about capital letters and small letters. If you made a variable called ```letter``` and another one called ```Letter``` Python would treat these as *completely separate* variables.

-----

- That's enough for the first step in Python coding. Take a break, or go on to [step 2](../step2/step2.md).

- Back to [front page](../README.md)
