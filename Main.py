import time as T
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import random as R
SPEED = 1e-999999
#Calling the variable:

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
tom = Snake()
tom.create_snake()
food = Food()
scoreboard = Scoreboard()


#Make the snake move - Funct create on snake.py

screen.listen()
screen.onkey(tom.up, "z")
screen.onkey(tom.down, "s")
screen.onkey(tom.left, "d")
screen.onkey(tom.right, "q")

#Activation of the game
game_is_on = True
while game_is_on:
    screen.update()
    T.sleep(SPEED)
    tom.move()
    #Detect collision with food
    if tom.head.distance(food.pos()) < 15:
        food.refresh()
        scoreboard.hideturtle()
        tom.extend()
        scoreboard.increase_score()
        SPEED *= 1e-10000

    #Detect collision with wall
    if tom.head.xcor() > 280 or tom.head.xcor() < -280 or tom.head.ycor() > 280 or tom.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    #Detect collision with the tail
    if tom.eat_Tails():
        game_is_on = False
        scoreboard.game_over()

screen.mainloop()