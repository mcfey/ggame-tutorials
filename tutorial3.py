from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, green)
bg = Sprite(bg_asset, (0,0))

# A ball! This is already in the ggame-tutorials repository
ball_asset = ImageAsset("images/orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))
# Original image is too big. Scale it to 1/10 its original size
ball.scale = 0.1
# custom attributes
ball.dir = 1
ball.go = True

def reverse(b):
    b.dir *= -1
def step():
    if ball.go:
        ball.x += ball.dir
        if ball.x + ball.width > SCREEN_WIDTH or ball.x < 0:
            ball.x -= ball.dir
            reverse(ball)

myapp.run(step)