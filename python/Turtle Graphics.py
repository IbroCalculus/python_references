import turtle
import time

def runTurtle():
    turtle.title("This is the title")
    turtle.penup()
    turtle.setposition(0,0)    #0,0 is center of screen, also -x, -y
    turtle.setheading(45)           #setheading(angle): sets the pen to face in a particular direction
    turtle.pencolor("#ff0000")
    turtle.pendown()
    turtle.forward(200)         #forward right direction
    turtle.left(90)
    time.sleep(1)

    turtle.pencolor("#0000ff")
    turtle.forward(150)
    turtle.left(90)
    time.sleep(1)
    turtle.pensize(4)
    turtle.hideturtle()

    turtle.pencolor("#00ff00")
    turtle.forward(200)
    turtle.left(90)
    time.sleep(1)
    turtle.pensize(10)

    turtle.pencolor('#123456')
    turtle.forward(150)
    time.sleep(2)
    turtle.exitonclick()

runTurtle()

#REFERENCE; HALTERMAN
#Other methods
#speed(arg)       0 == 'fastest', 10 == 'fast', 6 == 'normal', 3 == 'slow', 1 == 'slowest'
#setheading(angle): sets the pen to face in a particular direction
#setposition(x,y)       0,0 is center of screen