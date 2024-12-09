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

(Don't forget the brackets after the word Screen, and be sure you use a capital S.) Our project now contains a *new* type of Python object - not a number or a text string, but a *Turtle Screen* object. If you use ```type(s)``` to investigate the type of the variable ```s``` you will find it is of type ```Screen```.

We chose ```s``` as the variable name for our screen, but you can use *any* Python variable name which follows the rules for the screen.

We can set the size of our graphics screen in *pixels*. In the code below we specify a size of 400 pixels across, and 400 pixels from top to bottom.

We can also specify the background colour of our screen - here we have used *lightblue*. But notice that the line of code which sets the colour needs to use the American spelling *color*.

``` python
s.setup(400,400)
s.bgcolor('lightblue') # short for background color
```

Click on **Run** and you should see a light blue square shape in the place where you normally see printed results.

![Turtle screen](turtle1.png)

If your screen is quite small and you can't see the whole of the square you can actually *drag* the bar between the editing window and the results panel from side to side. Make sure you can see the complete coloured square.

The screen has a ***coordinate system***. This works in a similar way to Scratch coordinates with x = 0, y = 0 as the point in the middle of the screen. In our case the size of the screen is 400 pixels in both directions, which means the minimum x coordinate (at the left edge) is -200, and the maximum x coordinate (at the right edge) is +200. Similarly for y coordinates, the minimum (at the bottom) is -200 and the maximum (at the top) is +200.

## A turtle to do the drawing

Our graphics programming will consist of making sprites, called *turtles*, and moving them around the screen, sometimes drawing lines behind them and sometimes not.

Here is some code to make our first ever turtle:

``` python
t = Turtle()
```

This is exactly the same code as we used to make variables before - for example, ```myname = "Hagrid"``` - the difference is that we are not making a text string for our variable, we are making a *Turtle* object.

We've used a variable name ```t``` for this turtle, but (as with the Screen) you can use *any* valid variable name for a turtle.

Now that we've made a turtle object, and linked it to a variable, we have access to a whole lot of turtle functions to set and control our turtle object.

One thing we can do is set the shape for our turtle object. Here is the code to set it to the shape of a turtle

``` python
t.shape('turtle')
```

If you click Run you will now see your turtle!

![Turtle on screen](turtle2.png)

Other shapes you can try for your turtle are ```'arrow', 'circle', 'square', 'triangle', 'classic'```. Don't forget: you need to put quotes around these shapes.

You can also change the colour of your turtle. (Again, look out for using the American spelling color.)

``` python
t.color('green')
```

Click Run to see the results. There is a huge range of colours you can use for your turtles (and screens). [This web page](https://trinket.io/docs/colors) has a useful list of all the available colours. Click on a square to see what the colour is called.

-----

- When you're ready, go on to the [next step](../step4/step4.md) and find out about Python lists, while writing a *Hogwarts Sorting Hat* programme.

- Back to [previous step](../step3/step3.md).

- Back to [front page](../README.md)
