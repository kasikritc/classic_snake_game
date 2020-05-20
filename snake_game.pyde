from Snake import *
from Target import *

SQUARESIZE = 20
WIDTH = 35 # number of squares that can fit the width of the screen
HEIGHT = 35 # number of squares that can fit the height of the screen

def setup():
    size(SQUARESIZE*WIDTH, SQUARESIZE*HEIGHT)
    background(0)
    
    global snake, apple, isGameOver
    snake = Snake()
    apple = Target()
    isGameOver = False

def draw():
    global snake, apple, isGameOver
    frameRate(15)
    background(0)
    
    if isGameOver:
        fill(255)
        textSize(48)
        text("Game Over", width/2-125, height/2-150)
        textSize(28)
        text("Press 'R' to play again", width/2-150, height/2-100)
        
        snake.show()
        apple.show()
    else:
        snake.show()
        snake.update_loc()
        apple.show()
        # print(snake.body[0])
        if apple.is_snake_collide(snake):
            apple.change_pos()
        if snake.is_collide_with_self():
            isGameOver = True
    
def keyPressed():
    if keyCode == UP or keyCode == DOWN or keyCode == LEFT or keyCode == RIGHT or \
        keyCode == 87 or keyCode == 65 or keyCode == 83 or keyCode == 68:
        # ASCII of 'w' is 87, 'a' is 65, 's' is 83, 'd' is 68
        snake.change_dir(keyCode)
        
        
