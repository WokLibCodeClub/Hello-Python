# Example of Python multiple test ```if``` block

This is a simple example to show how a multiple test ```if``` block works, and also to show that the order of carrying out the tests is very important.

Start a new trinket project following the instructions [here](../trinket_basics/using_trinket.md#starting-a-new-trinket-project) and add this code at the beginning:

``` python
#!/bin/python3

from turtle import *

s = Screen()
s.setup(300,300)
s.bgcolor('grey')

# This line sets up a custom turtle shape - a big square
s.register_shape('big square', ((-50,50),(50,50),(50,-50), (-50,-50)))

t = Turtle()
t.shape('big square')

#########################################################
# This is where we will start the project

reading = 42
```

-----

- Back to [Sorting Hat code](../step4/step4.md#sorting-hat).

- Back to [front page](../README.md)
