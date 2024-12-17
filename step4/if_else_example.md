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

This code is going to make a big square turtle into a multi-coloured warning light, where it will change colour if our variable ```reading``` gets too high. Let's say if ```reading``` is above 90 we show a red light for danger, if it's between 71 and 90 we show an orange light, 51 to 70 we show a yellow light, and below 51 we show a green light.

How do we write the code to put this into action?

One way would be to have a lot of separate ```if``` blocks:

``` python
if reading > 90:
    t.color('red')

if reading > 70:
    t.color('orange')

if reading > 50:
    t.color('yellow')
else:
    t.color('lime green')
```

To test this code change the value of variable ```reading``` and run the code lots of times to see if it's showing the correct colour.

In fact, this code isn't working at all well - any value of reading above 50 makes the colour yellow, and we never see the orange and red colours at all.

What's happening is that if the reading is above 90 then the first ```if``` test is ```True```, so the colour changes to red, but immediately afterwards Python does the second test. If the reading is above 90 then it must also be above 70, so, before you can see it, the colour changes to orange. Then Python does the third test - and if the reading is above 90 it's also above 50, so the colour changes instantly to yellow, which is the colour we see.

There are two ways to fix this.

## 1. Using ```elif```

If we combine all these ```if``` blocks into one multiple block using ```elif``` we can take advantage of the way Python carries out multiple tests, especially the fact that as soon as it finds a test which is ```True``` it immediately skips all the other tests.

Change the second and third ```if``` to ```elif``` and try the code again. You should now find the turtle always shows the correct colour as you vary the value of ```reading```.

So, if the reading is, say, 99, the first test gives ```True```, so the colour is set to red, and Python immediately skips all the other tests, leaving the red colour showing.

If the reading is 75 the first test gives ```False```, so Python goes on to the second test - this one gives ```True``` so the colour is set to orange, and Python skips the remaining tests, so the colour stays orange.

## 2. Changing the order of the tests

Using ```elif``` is definitely the best way of fixing the problem, but you *can* do it using just ```if``` blocks by changing the order of doing the tests.

In this example the way to do this is to test for the lowest value first and then work upwards:

``` python
if reading > 50:
    t.color('yellow')

if reading > 70:
    t.color('orange')

if reading > 90:
    t.color('red')
else:
    t.color('lime green')
```

If reading was, say, 95 the first test would give ```True``` (reading > 50, so colour would be set to yellow) then immediately move to the second test which would also give ```True``` (reading > 70, so the colour is immediately reset to orange) then finally it would also give ```True``` for the third test, because reading > 90, so colour would finally be set to red - which is what we want.

But although the code now works it's clear that Python is doing a lot of unnecessary testing here. That's why the ```elif``` option is a more efficient way of coding for this example.

-----

- Back to [Sorting Hat code](../step4/step4.md#sorting-hat).

- Back to [front page](../README.md)
