import pyxel
import random

STATE = ['start', 'playing', 'paused', 'game_over']
class Snake_Game:
    def __init__(self):
        # ---------------- Window Settings ---------------- #
        self.state = 'start'
        # Background color used when clearing the screen.
        self.bg_color = 5

        # Window dimensions.
        self.window_height = 180
        self.window_width = 180

        # Create the game window.
        pyxel.init(
            self.window_width,
            self.window_height,
            title="Hello Snake"
        )

        # ---------------- Snake ---------------- #

        # Current head position.
        # (Eventually this can be replaced by self.snake_coord[0])
        self.snake_x = 90
        self.snake_y = 90

        # Current direction of movement.
        #
        # (1,0)  -> Right
        # (-1,0) -> Left
        # (0,-1) -> Up
        # (0,1)  -> Down
        self.dir_x = 1
        self.dir_y = 0

        # ---------------- Apple ---------------- #

        # Spawn the apple at a random position.
        # Step = 1 is the default, so we don't need to specify it.
        self.apple_x = random.randrange(1, 170)
        self.apple_y = random.randrange(1, 170)

        # ---------------- Snake Body ---------------- #

        # The snake is represented as a list.
        #
        # Every element is one body segment:
        #
        # [
        #     [head_x, head_y],
        #     [body_x, body_y],
        #     [tail_x, tail_y]
        # ]
        #
        # Initially the snake only has one segment (its head).
        self.snake_coord = [
            [self.snake_x, self.snake_y]
        ]

        # Start the Pyxel game loop.
        pyxel.run(self.update, self.draw)

    def update(self):

        if self.state == 'start':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = 'playing'
            elif pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
        # ---------------- Keyboard Input ---------------- #
        elif self.state == 'game_over':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = 'start'
        elif self.state == 'paused':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = 'playing'
        elif self.state == 'playing':
            if pyxel.btnp(pyxel.KEY_TAB):
                self.state = 'paused'
            # Quit the game when Q is pressed.
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

            # Change direction.
            #
            # The second condition prevents the snake from
            # immediately reversing into itself.
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

            # ---------------- Self Collision ---------------- #

            # Compare the head with every body segment.
            # If they occupy the same position,
            # the snake has collided with itself.
            #
            # Pythonic alternative:
            #
            # if self.snake_coord[0] in self.snake_coord[1:]:
            #     pyxel.quit()
            for coord in self.snake_coord[1:]:
                if coord == self.snake_coord[0]:
                    self.state = 'game_over'
                    #pyxel.quit()

            # ---------------- Screen Wrapping ---------------- #

            # If the snake leaves one side of the screen,
            # make it appear on the opposite side.

            if self.snake_x >= self.window_width:
                self.snake_x = 0

            elif self.snake_x <= 0:
                self.snake_x = self.window_width

            if self.snake_y >= self.window_height:
                self.snake_y = 0

            elif self.snake_y <= 0:
                self.snake_y = self.window_height

            # ---------------- Move Snake ---------------- #

            # Move the head according to the current direction.
            self.snake_x += self.dir_x
            self.snake_y += self.dir_y

            # ---------------- Apple Collision ---------------- #

            # Check whether the head overlaps the apple.
            #
            # Chained comparisons are the Pythonic way of
            # checking if a value lies inside a range.
            if (
                self.snake_x <= self.apple_x <= self.snake_x + 4
                and
                self.snake_y <= self.apple_y <= self.snake_y + 4
            ):

                # Spawn a new apple.
                self.apple_x = random.randrange(1, 170)
                self.apple_y = random.randrange(1, 170)

                # Add the new head.
                #
                # Since we DO NOT remove the tail,
                # the snake grows by one segment.
                self.snake_coord.insert(
                    0,
                    [self.snake_x, self.snake_y]
                )

            else:

                # Normal movement.
                #
                # 1. Add a new head.
                self.snake_coord.insert(
                    0,
                    [self.snake_x, self.snake_y]
                )

                # 2. Remove the old tail.
                #
                # The snake keeps the same length,
                # but appears to move forward.
                self.snake_coord.pop()


    def draw(self):

        # ---------------- Draw Frame ---------------- #

        # Clear everything drawn in the previous frame.
        pyxel.cls(self.bg_color)

        if self.state == 'start':
            pyxel.text(50, 50, "Press Space to Play", 15) 
        elif self.state == 'paused':
            pyxel.text(50, 50, "Press Space to Unpause", 15) 
        elif self.state == 'game_over':
            pyxel.text(50, 50, "Press Space to Go to Menu", 15) 
        elif self.state == 'playing':
        # Draw every segment of the snake.
        #
        # "segment" is one list:
        #
        # [x, y]
        #
        # segment[0] -> x-coordinate
        # segment[1] -> y-coordinate
            for segment in self.snake_coord:
                pyxel.rect(
                    segment[0],
                    segment[1],
                    4,
                    4,
                    10
                )

            # Draw the apple.
            pyxel.circ(
                self.apple_x,
                self.apple_y,
                1,
                8
            )


Snake_Game()


# import pyxel
# import random

# class Snake_Game:
#     def __init__(self):
#         self.bg_color = 5
#         self.window_height = 180
#         self.window_width = 180
#         pyxel.init(self.window_height, self.window_width, title = "Hello Snake")
#         self.snake_x =  90
#         self.snake_y = 90
#         self.dir_x = 1
#         self.dir_y = 0
#         self.apple_x = random.randrange(1, 170, 1)
#         self.apple_y = random.randrange(1, 170, 1)
#         self.snake_coord = [[self.snake_x, self.snake_y]]
#         pyxel.run(self.update, self.draw)

#     def update(self):
#         if pyxel.btnp(pyxel.KEY_Q):
#             pyxel.quit()
#         elif pyxel.btn(pyxel.KEY_LEFT) and self.dir_x != 1:
#             self.dir_x = -1
#             self.dir_y = 0
#         elif pyxel.btn(pyxel.KEY_RIGHT) and self.dir_x != -1:
#             self.dir_x = 1
#             self.dir_y = 0
#         elif pyxel.btn(pyxel.KEY_UP) and self.dir_y != 1:
#             self.dir_x = 0
#             self.dir_y = -1
#         elif pyxel.btn(pyxel.KEY_DOWN) and self.dir_y != -1:
#             self.dir_x = 0
#             self.dir_y = 1

#         for coord in self.snake_coord[1:]:
#             #head_coord = snake_coord[0]
#             if coord == self.snake_coord[0]:
#                 pyxel.quit()
#         '''
#                 # Pythonic way
#                 if self.snake_coord[0] in self.snake_coord[1:]:
#                     pyxel.quit()
#         '''
#         if self.snake_x >= self.window_width:
#             self.snake_x = 0
#         elif self.snake_x <= 0:
#             self.snake_x = 180

#         if self.snake_y >= self.window_height:
#             self.snake_y = 0
#         elif self.snake_y <= 0:
#             self.snake_y = 180
#         self.snake_x += self.dir_x            
#         self.snake_y += self.dir_y

#         if (self.snake_x <= self.apple_x <= self.snake_x + 4) and (self.snake_y <= self.apple_y <= self.snake_y + 4):
#             self.apple_x = random.randrange(1, 170, 1)
#             self.apple_y = random.randrange(1, 170, 1)
#             #self.snake_len += 1
#             self.snake_coord.insert(0, [self.snake_x, self.snake_y])
#         else:
#             self.snake_coord.insert(0, [self.snake_x, self.snake_y])
#             self.snake_coord.pop()

#     def draw(self):
#         pyxel.cls(self.bg_color)
#         #pyxel.text(50, 20, 'Welcome to the Game', 2)
#         for segment in self.snake_coord:
#             pyxel.rect(segment[0], segment[1], 4, 4, 10)
#         pyxel.circ(self.apple_x, self.apple_y, 1, 8)

# Snake_Game()

