from turtle import *


#we wanna paint a house


width(7)
speed(50)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of squareology

#door time!!!

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)


#roof time

penup()
goto(200, 200)
pendown()

color("blue")
right(150)
forward(200)
left(120)
forward(200)

penup()
goto(18, 160)
pendown() 
color("green")

left(120)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

penup()
goto(140,160)
pendown()

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)



exitonclick()