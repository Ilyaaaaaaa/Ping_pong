from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (width, height))
        self.speed = speed
        self.rect = (self.image.get_rect())
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_one(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < wh - 130:
            self.rect.y += self.speed
    

class Player_two(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < wh - 130:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update():

window = display.set_mode((1280, 800))
ww, wh = window.get_size()

game = True
finish = False
BLUE = (0, 80, 255)

player1 = Player_one("rocketka.png", 10, wh / 2 - 120, 20, 120, 10)
player2 = Player_two("rocketka.png", ww - 30, wh / 2 - 120, 20, 120, 10)

FPS = 60
clock = time.Clock()

while game:
    ww, wh = window.get_size()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(BLUE)
        player1.update()
        player2.update()
        player1.reset()
        player2.reset()
    clock.tick(FPS)
    display.flip()
