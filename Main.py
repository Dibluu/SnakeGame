import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
SPEED = 1e-999999999999999999999999999999
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
    time.sleep(SPEED)
    tom.move()
    #Detect collision with food
    if tom.head.distance(food.pos()) < 15:
        food.refresh()
        tom.extend()
        scoreboard.increase_score()
        SPEED *= 0.001

    #Detect collision with wall
    if tom.head.xcor() > 280 or tom.head.xcor() < -280 or tom.head.ycor() > 280 or tom.head.ycor() < -280:
        scoreboard.reset_score()
        tom.reset_snake()
    #Detect collision with the tail
    if tom.eat_Tails():
        scoreboard.reset_score()
        tom.reset_snake()

screen.mainloop()