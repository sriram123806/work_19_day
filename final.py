import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 500)

loop = True

user_ans = turtle.textinput("MAKE YOUR BIT :", "which turtle do you want to have,choose the color :")

colour = ["red", "blue", "green", "yellow", "violet", "orange"]
position = [-150,-100,-50,0,50,100]

turtles = []

for select in range(6):
    sri = Turtle()
    sri.shape("turtle")
    sri.penup()
    sri.color(colour[select])
    sri.goto(-230, position[select])
    turtles.append(sri)

if user_ans:
    loop = True

while loop:
    for nav in turtles:
        if nav.xcor() > 225 :
            loop = False
            winner = nav.pencolor()
            if winner == user_ans:
                print("YOU WON")
                print(f"WINNER IS : {winner}")
            else:
                print("YOU LOST")
                print(f"WINNER IS : {winner}")

        no = random.randint(0, 10)
        nav.forward(no)

screen.exitonclick()