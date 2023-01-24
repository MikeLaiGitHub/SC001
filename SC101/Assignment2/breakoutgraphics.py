"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.__dx = 0
        self.__dy = 0
        self.__count = 0
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'grey'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius, x=window_width/2, y=window_height/2)
        self.ball.filled = True
        self.ball.fill_color = 'lightblue'
        self.window.add(self.ball)
        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmouseclicked(self.move)
        onmousemoved(self.go)
        # Draw bricks
        k = 0
        n = 0
        global BRICK_COLS
        while n != 10:
            while BRICK_COLS >= 1:
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=BRICK_WIDTH*k+BRICK_SPACING*k,
                                   y=BRICK_OFFSET+BRICK_HEIGHT*n+BRICK_SPACING*n)
                self.brick.filled = True
                if n < 2:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 2 <= n < 4:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 4 <= n < 6:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 6 <= n < 8:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick)
                k += 1
                BRICK_COLS -= 1
            BRICK_COLS = 10
            k = 0
            n += 1

    def go(self, mouse):
        if mouse.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width/2
            # self.paddle.y = self.window.height - PADDLE_OFFSET - PADDLE_HEIGHT

    def move(self, mouse):
        if self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            self.ball.move(self.__dx, self.__dy)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def get_ball(self):
        return self.ball

    def get_count(self):
        return self.__count

    def bounce(self):
        if self.ball.y <= 0:    # when ball hit the top it bounce.
            self.__dy = -self.__dy
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:  # when ball hit the left/right wall.
            self.__dx = -self.__dx
        if self.ball.y < self.window.height/2:  # to get rid of the brick when the ball touches.
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
                self.__dy = -self.__dy
            if self.window.get_object_at(self.ball.x+BALL_RADIUS*2, self.ball.y) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x+BALL_RADIUS*2, self.ball.y))
                self.__dy = -self.__dy
            if self.window.get_object_at(self.ball.x, self.ball.y+BALL_RADIUS*2) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y+BALL_RADIUS*2))
                self.__dy = -self.__dy
            if self.window.get_object_at(self.ball.x+BALL_RADIUS*2, self.ball.y+BALL_RADIUS) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x+BALL_RADIUS*2, self.ball.y*BALL_RADIUS*2))
                self.__dy = -self.__dy
        else:   # This is for the bal to bounce when the ball touch the paddle.
            if self.window.get_object_at(self.ball.x+BALL_RADIUS*2, self.ball.y+BALL_RADIUS*2) is not None:
                self.__dy = -self.__dy

    def restart(self):  # The loop where the ball is suppose to stop after losing three lives.
        if self.ball.y >= self.window.height:
            self.ball = GOval(BALL_RADIUS, BALL_RADIUS, x=self.window.width / 2, y=self.window.height / 2)
            self.ball.filled = True
            self.ball.fill_color = 'lightblue'
            self.window.add(self.ball)
            self.__count += 1
