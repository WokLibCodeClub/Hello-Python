# Python Graphics

Now we can start to get Python drawing things on the screen.

For our first goes at doing graphics we will use a Python library called ```turtle``` which contains a lot of functions specially designed for drawing on the screen. There are sprites, a little bit like Scratch, but they are called ... ***Turtles!!***

Start a new project, following the instructions [here](../trinket_basics/using_trinket.md#starting-a-new-trinket-project) and add this code at the beginning:

``` python
#!/bin/python3

from turtle import *
```

When we used ```import``` before we specified individual functions to import from the libraries (for example: ```from time import sleep```), but here we want to use all the available functions in the turtle library, so the ```*``` sign indicates we want to import *everything*.

## A screen to draw on

The next line of code will create a graphics screen for our drawing. We will use a variable ```s``` with the graphics screen which allows us to apply special screen-functions to our screen using the variable name.

``` python
s = Screen()
```

(Don't forget the brackets after the word Screen.)

We can set the size of our graphics screen in *pixels*. In the code below we specify a size of 400 pixels across, and 400 pixels from top to bottom.

We can also specify the background colour of our screen - here we have used *lightblue*. But notice that the line of code which sets the colour needs to use the American spelling *color*.

``` python
s.setup(400,400)
s.bgcolor('lightblue')
```

Click on **Run** and you should see a light blue square shape in the place where you normally see printed results.

![Turtle screen](turtle1.png)

If your screen is quite small and you can't see the whole of the square you can actually *drag* the bar between the editing window and the results panel from side to side. Make sure you can see the complete coloured square.



-----

- When you're ready, go on to the [next step](../step4/step4.md) and find out about Python lists, while writing a *Hogwarts Sorting Hat* programme.

- Back to [previous step](../step3/step3.md).

- Back to [front page](../README.md)
