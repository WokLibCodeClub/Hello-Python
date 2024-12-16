#!/bin/python3

from turtle import *

s = Screen()
s.setup(400,400)
s.bgcolor('lightblue') # bgcolor is short for background color

t = Turtle()
t.shape('turtle')
t.pencolor('red')
t.fillcolor('yellow')

t.penup()
t.goto(-50,-50)
t.pendown()

num_sides = 7
size = 400 / num_sides

t.begin_fill()
counter = 0
while counter < num_sides:
  t.forward(size)
  t.left(360 / num_sides)
  counter += 1
t.end_fill()
