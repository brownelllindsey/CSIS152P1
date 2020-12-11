"""

Description:
This program will trace a train by first drawing a red rectangle for the body,
two black circle wheels, a blue square for the conductor's area, a black
square and a trapezoid for a steamblower, a green 30-60-90 triangle for the
front of the train, black lines to make up a stick-figure person, and an
orange line and a rectangle to create a sign. Inside this sign, you are able
to type your own message.

"""

__author__= "Lindsey Brownell"
__date__= "1/18/2019"
import turtle
wn = turtle.Screen()

from turtle import *
myWindow = Screen()


# Create Vehicle
train = turtle.Turtle()

# Rectangle
train.color("red")
train.begin_fill()
train.forward(100)      #Bottom Line
train.left(90)
train.forward(50)       #Right Side
train.left(90)
train.forward(100)      #Top Line
train.left(90)
train.forward(50)       #Left Side
train.end_fill()

# Wheel 1
train.penup()
train.left(90)
train.forward(20)
train.right(180)
train.pendown()
train.color("black")    
train.begin_fill()
train.circle(10)        #Left (Front) Wheel
train.end_fill()

# Wheel 2
train.penup()
train.left(180)
train.forward(60)
train.right(180)
train.pendown()
train.color("black")
train.begin_fill()
train.circle(10)        #Right (Back) Wheel
train.end_fill()
train.penup()

# Square
train.left(180)
train.forward(20)
train.left(90)
train.forward(50)
train.pendown()
train.color("blue")
train.begin_fill()
train.forward(40)       #Conductor's Suite, Right Side
train.left(90)
train.forward(40)       #Roof
train.left(90)
train.forward(40)       #Left side
train.left(90)
train.end_fill()

# Steam Blower
train.penup()
train.left(180)
train.forward(30)
train.pendown()
train.color("black")
train.begin_fill()
train.right(90)
train.forward(15)       #Right Side
train.right(45)
train.forward(10)       #Angled Line, Right side of Upside down trapezoid
train.left(135)
train.forward(30)       #Top of Steamblower
train.left(135)
train.forward(10)       #Angled Line, Left side of Upside down trapezoid
train.right(45)
train.forward(15)       #Left Side
train.end_fill()
train.penup()

# Triangle (front of train)
train.right(90)
train.forward(15)
train.left(60)
train.pendown()
train.color("green")
train.begin_fill()
train.forward(58)       #Front (Left) Side of Triangle
train.left(120)
train.forward(30)       #Bottom of Triangle
train.end_fill()
train.penup()

# Create Person
train.left(180)
train.forward(90)
train.color("black")
train.pendown()
train.left(45)
train.forward(15)       #Left Leg
train.left(180)
train.forward(15)
train.right(90)
train.forward(15)       #Right Leg
train.right(180)
train.forward(15)
train.right(45)
train.forward(30)       #Body
train.left(90)
train.forward(15)       #Left Arm
train.left(180)
train.forward(15)
train.left(90)
train.forward(10)       #Neck
train.right(90)
train.circle(7)         #Head
train.right(90)
train.forward(10)
train.left(90)
train.forward(15)       #Right Arm

# Create Sign
train.left(70)
train.color("orange")
train.forward(45)       #Stick
train.right(70)
train.forward(20)       #Creating Rectangular Sign, Bottom Right
train.left(90)
train.forward(20)       #Right Side of Sign
train.left(90)
train.forward(40)       #Top of Sign
train.left(90)
train.forward(20)       #Left Side of Sign
train.left(90)
train.forward(20)       #Bottom Left

# Message
train.left(180)         #Moving Pen to middle of sign for message
train.forward(20)
train.right(90)
train.forward(10)
train.right(90)
train.penup()
train.forward(3)
train.pendown()
message = myWindow.textinput("Message Input", "Please Enter Your Message: ")
train.write(message)

myWindow.exitonclick()




