from turtle import Turtle, Screen

tom = Turtle(shape="turtle")
screen = Screen()

def move_forwards():
    tom.forward(10)

def move_backwards():
    tom.backward(10)


def turn_right():
    new_heading = tom.heading()+10
    tom.setheading(new_heading)

def turn_left():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)


def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(move_forwards, "f")
screen.onkey(move_backwards, "b")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clear_screen, "c")

screen.exitonclick()