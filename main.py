from turtle import Screen,Turtle



sri = Turtle()
screen = Screen()
sri.shape("turtle")
sri.pensize(10)

def move_forwards():
    sri.forward(10)
def move_forwards1():
    sri.back(10)
def move_forwards2():
    sri.right(45)
def move_forwards3():
    sri.circle(90)
def move_forwards4():
    sri.tilt(90)
    sri.forward(20)
def move_forwards5():
    sri.left(45)
def clear_scr():
    sri.clear()
    sri.penup()
    sri.home()
    sri.pendown()


screen.listen()
screen.onkey(key ="f",fun =move_forwards)
screen.listen()
screen.onkey(key ="b",fun =move_forwards1)
screen.listen()
screen.onkey(key ="r",fun =move_forwards2)
screen.listen()
screen.onkey(key ="a",fun =move_forwards3)
screen.listen()
screen.onkey(key ="t",fun =move_forwards4)
screen.listen()
screen.onkey(key ="l",fun =move_forwards5)
screen.listen()
screen.onkey(key ="c",fun =clear_scr)
screen.exitonclick()

