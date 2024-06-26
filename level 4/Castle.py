from turtle import *

title("GOA Castle")
width(4)
speed(0)
color("gray")

forward(620)
left(90)

forward(300)
left(90)
forward(80)
penup()
goto(300, 60)
left(90)

forward(60)
left(90)
pendown()
backward(300)
left(90)

forward(300)
right(90)

forward(100)
right(90)

forward(160)
left(90)
forward(80)
left(90)
forward(60)

right(90)
forward(80)
left(90)
forward(140)

right(90)
forward(100)
right(90)
forward(140)
left(90)
forward(80)

right(90)
forward(50)

left(90)
forward(80)

left(90)
forward(150)
right(90)
forward(20)
penup()
goto(20, 80)
pendown()

color("green")
left(90)
forward(200)
right(90)
forward(60)

right(90)
forward(200)
goto(50, 120)
goto(20, 80)

penup()
goto (600, 100)
right(90)
right(90)
pendown()
forward(180)

left(90)
forward(60)

left(90)
forward(180)

goto (570, 140)
goto (600, 100)
penup()

penup()
color("brown")
goto(260, 150)
shape("square")
pendown()
forward(150)
left(90)
forward(100)
left(90)
forward(150)
left(90)
forward(100)
left(90)

penup()
color("black")
goto(310, 340)
right(90)
right(90)
pendown()

forward(50)
goto(310, 365)
goto(310, 420)
left(90)
forward(97)
left(90)
forward(65)
left(90)
forward(97)
left(35)
penup()


goto(230, 370)
pendown()
write("GOA", font=("Cursive", 20, "italic"))
penup()
goto(69, 420)
color("yellow")
turtlesize(5,5,5)
shape("circle")

sc = Screen() 
sc.setup(400, 300) 
textinput("Please rate", "X/10") 

exitonclick()