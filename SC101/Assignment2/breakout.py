"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    while True:
        graphics.bounce()
        x_speed = graphics.get_dx()
        y_speed = graphics.get_dy()
        graphics.ball.move(x_speed, y_speed)
        pause(FRAME_RATE*1.5)
        # when used up all the lives attempting to break the loop.
        if graphics.get_count() == NUM_LIVES:
            break
        else:
            graphics.restart()


if __name__ == '__main__':
    main()
