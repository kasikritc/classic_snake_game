SQUARESIZE = 20
WIDTH = 35 # number of squares that can fit the width of the screen
HEIGHT = 35 # number of squares that can fit the height of the screen

class Target:
    '''
    @attributes:
        pos = (PVector) x and y coordinates of the Target
    '''
    def __init__(self):
        self.pos = PVector(int(random(WIDTH)), int(random(HEIGHT)))
        # print(self.pos.x, self.pos.y)
    
    def show(self):
        fill(255)
        rect(self.pos.x*SQUARESIZE, self.pos.y*SQUARESIZE, 20, 20)
    
    def change_pos(self):
        self.pos = PVector(int(random(WIDTH)), int(random(HEIGHT)))
    
    def is_snake_collide(self, snake):
        if snake.body[0] == self.pos:
            snake.add_segment += 2
            return True
        return False
        
