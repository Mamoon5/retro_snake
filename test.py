import pyxel
import random

class Snake_Game:
    def __init__(self):
        self.bg_color = 5
        self.window_height = 180
        self.window_width = 180
        pyxel.init(self.window_height, self.window_width)
        self.snake_x =  90
        self.snake_y = 90
        self.dir_x = 1
        self.dir_y = 0
        self.apple_x = random.randrange(1, 170, 1)
        self.apple_y = random.randrange(1, 170, 1)
        self.snake_coord = [[self.snake_x, self.snake_y]]
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_LEFT) and self.dir_x != 1:
            self.dir_x = -1
            self.dir_y = 0
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.dir_x != -1:
            self.dir_x = 1
            self.dir_y = 0
        elif pyxel.btn(pyxel.KEY_UP) and self.dir_y != 1:
            self.dir_x = 0
            self.dir_y = -1
        elif pyxel.btn(pyxel.KEY_DOWN) and self.dir_y != -1:
            self.dir_x = 0
            self.dir_y = 1

        if self.snake_x >= self.window_width:
            self.snake_x = 0
        elif self.snake_x <= 0:
            self.snake_x = 180

        if self.snake_y >= self.window_height:
            self.snake_y = 0
        elif self.snake_y <= 0:
            self.snake_y = 180
        self.snake_x += self.dir_x            
        self.snake_y += self.dir_y

        if (self.snake_x <= self.apple_x <= self.snake_x + 4) and (self.snake_y <= self.apple_y <= self.snake_y + 4):
            self.apple_x = random.randrange(1, 170, 1)
            self.apple_y = random.randrange(1, 170, 1)
            #self.snake_len += 1
            self.snake_coord.insert(0, [self.snake_x, self.snake_y])
        else:
            self.snake_coord.insert(0, [self.snake_x, self.snake_y])
            self.snake_coord.pop()

    def draw(self):
        pyxel.cls(self.bg_color)
        for segment in self.snake_coord:
            pyxel.rect(segment[0], segment[1], 4, 4, 10)
        pyxel.circ(self.apple_x, self.apple_y, 1, 8)

Snake_Game()