# First ever Python code

Use trinket to open a new project - this will be your first Python code, so give your project a name to show this.

The trinket window has two parts - to the left is the *coding panel* where you write your code; to the right is the *results panel* where the output of your code appears.

In Python code a lot of the words you type are followed by brackets: ```()``` and sometimes there are things typed inside the brackets, and sometimes they are empty.

When a word in Python is followed by brackets it means it is a Python ***function*** which means it carries out some action for us. At first we will use functions written by someone else, but later we will write our own functions.

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

Python calls letters and/or numbers inside quote marks a *text string*. A text string is a type of Python *object*. Python lets you use single quotes or double quotes to make a text string. 

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

Python has *two* types of number objects - whole numbers, called *integers*, which don't have any decimal values, and decimal numbers, called *floating point numbers* which have decimals. When Python does a division sum it *always* gives the answer as a decimal number, not a whole number.

You can do some things with integers that you can't do with decimal numbers, and vice versa.

## The Interactive Python Console

Open a new tab in your browser and go to this link:

[trinket.io/console](https://trinket.io/console)

This opens the Interactive Python Console, where the left end of each line begins with three *greater than* signs: ```>>>```.

You can use the console to try out Python code. It's really handy, because you can get it to show the result of your code without having to keep using the ```print()``` function.

In the console type:

```
2 + 4
```

and press Return. The console gives you the answer straight away.

You can combine different arithmetic operations.

In the console type

```
2 + 3 * 4
```

and try to predict the answer before you press Return.

Did you get it right? 

<details><summary>Click here if you didn't</summary>

<p></p>
If you thought the answer would be 20 you may have forgotten the rule BODMAS which tells you that you have to do multiplication <i>before</i> the addition.
<p></p>
How could you add a left and a right bracket to the sum so that the answer <i>would</i> be 20?
<p></p>
  
</details>

### Arithmetic with text strings

You can also do arithmetic with text strings. You can use + to add text strings together:

```
'Good' + 'morning'
```

but did you notice Python *didn't* put a space between the words this time?

You can multiply a text string by a number to repeat it. Here we make the computer laugh:

```
'Ha' * 10
```


