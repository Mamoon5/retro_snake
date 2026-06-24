# import pyxel

# pyxel.init(160, 120)

# def update():
#     if pyxel.btnp(pyxel.KEY_Q):
#         pyxel.quit()

# def draw():
#     pyxel.cls(0)
#     pyxel.rect(10, 10, 20, 20, 11)

# pyxel.run(update, draw)
import pyxel
import random
import time
class SnakeGame:
    def __init__(self):
        # 1. Initialize the game window (width, height, title)
        pyxel.init(180, 180, title="Retro Snake")

        # 2. Set an initial background color (1 = dark blue)
        self.bg_color = 1
        self.snake_x = 90 # Initial coordinates
        self.snake_y = 90
        self.dir_x = 2 # Moving two pixels at a time
        self.dir_y = 0 # Not moving up or down
        self.apple_coord_y = random.randrange(10, 170, 2)
        self.apple_coord_x = random.randrange(10, 170, 2)
        self.snake_segments = [[self.snake_x, self.snake_y]]
        self.snake_length = 1        
        # 3. Start the game loop (tells Pyxel which functions to run)
        pyxel.run(self.update, self.draw)

    def update(self):
        # Game logic goes here (runs 30 times a second)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.dir_x = -2
            self.dir_y = 0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.dir_x = +2
            self.dir_y = 0
        elif pyxel.btn(pyxel.KEY_UP):
            self.dir_x = 0
            self.dir_y = -2
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.dir_x = 0
            self.dir_y = +2

        self.snake_x += self.dir_x
        self.snake_y += self.dir_y
        # --- NEW SCREEN WRAPPING LOGIC ---
        if self.snake_x < 0:
            self.snake_x = 180
        elif self.snake_x > 180:
            self.snake_x = 0

        if self.snake_y < 0:
            self.snake_y = 180
        elif self.snake_y > 180:
            self.snake_y = 0
        self.snake_segments.insert(0, [self.snake_x, self.snake_y])
        if len(self.snake_segments) > self.snake_length:
            self.snake_segments.pop()
        if abs(self.snake_x - self.apple_coord_x) < 3 and abs(self.snake_y - self.apple_coord_y) < 3:
                # "Eat" the apple by moving it to a brand new random spot!
                self.apple_coord_x = random.randint(10, 170)
                self.apple_coord_y = random.randint(10, 170)
                #pyxel.rect(self.snake_x + 1, self.snake_y + 1, 6, 6, 10) 
                self.snake_length += 2
        # self.snake_x += 1
        # if pyxel.mouse(True):
        #     pass
    def draw(self):
        # Graphics drawing goes here
        pyxel.cls(self.bg_color)
        for segment in self.snake_segments:
            pyxel.rect(segment[0], segment[1], 6, 6, 10)
        #pyxel.rect(self.snake_x, self.snake_y, 6, 6, 10) 
        pyxel.circ(self.apple_coord_x, self.apple_coord_y, 2, 15)
        #self.draw_circ = pyxel.circ(self.apple_coord_x, self.apple_coord_y, 2, 15)
        '''
        pyxel.rect(x, y, w, h, col)
        Parameter Breakdownx: The x-coordinate of the rectangle's upper-left corner.y: The y-coordinate of the rectangle's upper-left corner.w: The width of the rectangle in pixels.h: The height of the rectangle in pixels.col: The color palette index (0–15) to fill the rectangle.
        '''
        # Print text at coordinates (x=10, y=10) with color 7 (white)
        pyxel.text(60, 10, "Press Q to Quit", 7)

# This actually starts the game when you run the script
SnakeGame()