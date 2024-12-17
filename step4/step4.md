# Lists and ```for``` loops

Start a new project, following the instructions [here](../trinket_basics/using_trinket.md#starting-a-new-trinket-project) and add this code at the beginning:

``` python
#!/bin/python3
```

This project will be for a Hogwarts School Sorting Hat, so you can give it a name to show that.

You will also find it useful to have the [Interactive Python Console](https://trinket.io/console) open in another tab of your browser.

## Sorting Hat

When new students arrive at Hogwarts School of Witchcraft and Wizardry they are divided into the school's different *houses*. They put on the *sorting hat*, which analyses their character and strengths and weaknesses and decides which house will suit them best.

We can't hope to do any of that with Python, so our Sorting Hat programme is a bit of a cheat, and just picks a house at random.

We'll start by writing a rather long and clumsy piece of code, and then show how we can make it much shorter by using a type of Python object called a *list*.

If we're going to pick a house at random then we will need to import from the ```random``` library the function ```randint```, which generates a random integer. Look back at your previous projects and see if you can find one which uses this function. Copy the line of code which contains the word ```import``` and paste it in at the beginning of the new project.

<details><summary>If you're <i>really</i> not sure how to do this...</summary>
<br>
Copying code from another project (your own or someone else's) is a very good way of getting familiar with Python, so you will be helping yourself if you get used to doing this.
<p></p>
Here is the line of code you need:
<p></p>

``` python
from random import randint
```
  
</details>

Since there are four houses in Hogwarts School we will generate a random integer between 1 and 4 and use this to select a house. Put the random integer in a variable. You can pick any name for the variable but it would be useful to have a name that indicates this is a random number. (WARNING: *don't* use the name ```randint``` as this is the name of a function, and you should avoid giving variables the same names as functions.) Look back at previous code if you aren't sure how to do this. (You will find a clue in [step 1](../step1/step1.md#python-libraries) in the section on Python libraries.)

Now we will make a rather complicated ```if ... else``` block to select the house. In the code below you need to put the name of your random number variable in place of the four asterisks:

``` python
if **** == 1:
  house = 'Hufflepuff'
elif **** == 2:
  house = 'Slytherin'
elif **** == 3:
  house = 'Gryffindor'
else:
  house = 'Ravenclaw'

print(house)
```

If you Run the code several times, it will print one of the four Hogwarts houses at random.

The words ```if``` and ```else``` we have already used in the *Age Calculator* code, but we haven't come across ```elif``` before.

```elif``` is short for 'else if' and it's a way of testing more than one statement inside a Python ```if``` block. If you work through this code you will see that it is testing for all the possible values of the random number. If it's a 1 (the line beginning ```if```) then we will select the house 'Hufflepuff', but if it's not a 1 it could still be 2, 3 or 4. The next line, beginning with ```elif```, now tests to see if it's a 2, in which case the house will be 'Slytherin'. But the random number could still be 3 or 4, so we need to do yet another test. First we test if it's a 3, with another ```elif``` line, which will make the house 'Gryffindor'. Finally, if the random number is not 1, 2 or 3, then it *must* be 4, so we don't need to test it - we just say ```else```, which means all the other tests have failed, in which case the house is 'Ravenclaw'.

A key feature of these multiple test ```if``` blocks is that as soon as Python finds one of the tests which is ```True``` it carries out the code for that test and skips the rest of the tests. In some circumstances this can save a lot of time.

In a Python ```if``` block the first line has to start with ```if```. If you have an ```else:``` line it has to go at the end (but you don't have to have one). In between, you can put as many ```elif``` blocks as you need.

## Lists in Python

Well that's the rather clumsy version of the Sorting House code. But we can make it much simpler using a Python *list*. Move the the browser tab with the [Interactive Python Console](https://trinket.io/console).

We are going to create a list, so type this into the console

``` python
houses = ['Hufflepuff', 'Slytherin', 'Gryffindor', 'Ravenclaw']
```

The first part of this code is simply making a variable, called ```houses```. To the right of the equals sign we have left and right *square brackets* ```[ ]``` and in between these we have a list of the different houses, each one separated by a comma. The square brackets indicate that we are making a *list*, so the variable ```houses``` will be of type "list".

We can print a list using the ```print()``` function:

``` python
print(houses)
```

which will print out all the items including the square brackets.

### Identifying the items in a list

Often we want to carry out some operation on just one item in a list, so we need a way to identify each of the items. The items in a list are each given an identifier, or ***index*** number, but be careful! You might think the first item in the list would have an index number 1 but it doesn't - the first item has the index number 0, and the index numbers increase from there.

In our ```houses``` list, the item 'Gryffindor' would have the index number 2, so if we wanted to print this we would type:

``` python
print(houses[2])
```

As you see we can refer to any item by using the variable name, followed by the index number in square brackets.

Try typing

``` python
print(houses[4])
```

![Index Error](index_error.png)

As you can see this produces an error - an "Index" error. This is a very common error, and almost all coders will accidentally create these at some time - it simply means you have tried to use a list with an index number which doesn't exist. Why did we cause this error? It's because although our list has four items the index numbers start at 0, so the last item in the list has index number 3, not 4. There is *no* item with an index number 4, so we get an error.

### Things you can do with lists

Now we've made a list we have opened the possibility of using a whole lot of special *list* functions in Python.

## The Python ```for``` loop

## The very useful ```range()``` function

## A turtle game with our own function

-----

- That's the end of our short introduction to Python. I hope you enjoyed it.

- Back to [previous step](../step3/step3.md).

- Back to [front page](../README.md)
