SQUARESIZE = 20
WIDTH = 35 # number of squares that can fit the width of the screen
HEIGHT = 35 # number of squares that can fit the height of the screen

class Snake:
    '''
    @attributes:
        body = (list) storing the x and y coordinates according of each segment to box number 
               (not according to the pixels)
        dir = (int) direction of head segment
        COLOR = (const) color of the snake
    '''
    def __init__(self):
        self.body = [PVector(int(random(10, WIDTH-10)), int(random(0, HEIGHT-7)))]
        for i in range(1, 6):
            self.body.append(PVector(self.body[0].x, self.body[0].y+i))
        self.dir = None
        self.COLOR = "#25FF25"
        self.add_segment = 0
    
    def show(self):
        '''
        @param: -
        @function: draw snake on screen
        @return: void
        '''
        # print(self.body[0].x, self.body[0].y)
        for segment in self.body:
            fill(self.COLOR)
            rect(segment.x*SQUARESIZE, segment.y*SQUARESIZE, 
                SQUARESIZE, SQUARESIZE)
    
    def change_dir(self, dir):
        '''
        @param: (int) dir
        @function: change direction of snake
        @return: void
        '''
        if (dir == UP or dir == 87) and dir != DOWN: self.dir = UP
        elif (dir == DOWN or dir == 83) and dir != UP: self.dir = DOWN
        elif (dir == LEFT or dir == 65) and dir != RIGHT: self.dir = LEFT
        elif (dir == RIGHT or dir == 68) and dir != LEFT: self.dir = RIGHT
    
    def update_loc(self):
        '''
        @param: -
        @function: update the location of snake
        @return: void
        '''
        head = self.body[0] # head.type = PVector(x, y)
        
        if self.dir == UP: 
            self.body.insert(0, PVector(head.x, head.y - 1))
            if self.add_segment > 0:
                self.add_segment -= 1
            else:
                self.body.pop(-1)
        elif self.dir == DOWN: 
            self.body.insert(0, PVector(head.x, head.y + 1))
            if self.add_segment > 0:
                self.add_segment -= 1
            else:
                self.body.pop(-1)
        elif self.dir == LEFT: 
            self.body.insert(0, PVector(head.x - 1, head.y))
            if self.add_segment > 0:
                self.add_segment -= 1
            else:
                self.body.pop(-1)
        elif self.dir == RIGHT:
            self.body.insert(0, PVector(head.x + 1, head.y))
            if self.add_segment > 0:
                self.add_segment -= 1
            else:
                self.body.pop(-1)
    
    def check_out_of_bounds(self):
        pass
        
    def is_collide_with_self(self):
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head == self.body[i]:
                return True
        return False
        
