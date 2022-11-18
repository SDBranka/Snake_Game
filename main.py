from turtle import Screen
from snake import Snake
import time

# build Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game V1")
screen.tracer(0)

snake = Snake()
# food = Food()

# enable screen to "listen" keystrokes
screen.listen()
# establish keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # updates the screen after each move
        # placed outside of the move loop
        # prevents seeing each independent segment move individually
    screen.update()
    # delays the time cycle of each move by 0.1 second
    time.sleep(0.1)

    snake.move()


screen.exitonclick()