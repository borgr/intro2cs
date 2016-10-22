#############################################################
# FILE : HelloTurtle.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex0 200132014
# DESCRIPTION:
# A simple program that prints "Hello World" using Turtle graphics
#############################################################
import turtle
# title for the display window
turtle.title("Fun with Turtle Graphics and Python")
turtle.up() # lift the pen up, no drawing
turtle.goto(-100,-100)
turtle.down() # pen is down, drawing now
# draw a square
turtle.goto(100,-100)
turtle.goto(100,100)
turtle.goto(-100,100)
turtle.goto(-100,-100)
# draw a circle
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.circle(100)
# go to the center, leave a message
turtle.up()
turtle.goto(-70,-5)
turtle.write("Hello World",font=("Arial", 20, "normal"))
turtle.done()
