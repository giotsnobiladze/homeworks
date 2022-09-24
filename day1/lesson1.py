from turtle import *


# we want to paint a house


#step1 : draw a squar

speed(15)


width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

# end of square

# draw a door
begin_fill()

forward(70)
color("brown")
left(90)

forward(90)
right(90)

forward(60)
right(90)

forward(90)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# draw a window (left)
begin_fill()

width(3)
penup()
goto(50, 100)
pendown()
color("green")
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


# draw a window (right)
begin_fill()
color("green")
penup()
goto(150, 100)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()



exitonclick()