
from turtle import Turtle, Screen
import time
import random
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("myfirst_snakegame")

# Positions for our three square snake
positions=[(0,0), (-20,0), (-40,0)]

# Creating empty list to append later
segment=[]

screen.tracer(0)

# creation of object scoreboard from scoreboard() class
scoreboard = Scoreboard()

# Creating three square shapes which is an snake and appending to our segment list
for segments in range(0,3):
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(positions[segments])
    segment.append(snake)


# randomization for our foods to be displayed to a new location for each succesive process
randomfood_x = random.randint(-280,280)
randomfood_y = random.randint(-280,280)

# Creating food
food = Turtle("circle")


# creating snake function to later call this function to change the position of our food
def snakefood():
    food.penup()
    food.color("blue")
    return food.goto(randomfood_x,randomfood_y)


snakefood()


headofsnake = segment[0]
# Controlling the movement with keys
upp = 90
downn = 270
leftt = 180
rightt = 0
def up():
    if headofsnake.heading() != downn:
        headofsnake.setheading(upp)

def down():
    if headofsnake.heading()!= upp:
        headofsnake.setheading(downn)

def right():
    if headofsnake.heading()!=leftt:
        headofsnake.setheading(rightt)

def left():
    if headofsnake.heading()!=rightt:
        headofsnake.setheading(leftt)

screen.onkey(key="w", fun=up)
screen.onkey(key="s", fun=down)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)




#To access score
score = 0

# Run the game until game_on is false
game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    screen.listen()



    for segments in range(len(segment) - 1, 0, -1):
        new_x = segment[segments - 1].xcor()
        new_y = segment[segments - 1].ycor()
        segment[segments].goto(new_x, new_y)

    segment[0].forward(15)
    lengthofsnake=len(segment)

    for seg in range(1, lengthofsnake):
        if headofsnake.distance(segment[seg]) < 10:
            headofsnake.goto(0, 0)
            game_on = False
            scoreboard.gameover()
# Collision with walls
    if headofsnake.xcor() > 290 or headofsnake.xcor() < -290 or headofsnake.ycor() > 290 or headofsnake.ycor() < -290:
        print("Game over")
        game_on=False
        print(score)
        scoreboard.gameover()


# Collision with food
    if headofsnake.distance(food) < 15:
        randomfood_x = random.randint(-280, 280)
        randomfood_y = random.randint(-280, 280)
        food.goto(randomfood_x, randomfood_y)
        scoreboard.clear()
        scoreboard.increase_score()
        score += 1
        new_seg=Turtle()
        new_seg.penup()
        new_seg.clear()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        segment.append(new_seg)


screen.exitonclick()