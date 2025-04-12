from pygame import *
from random import choice

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (width, height))
        self.speed = speed
        self.speed_x = choice([-5, 5])
        self.speed_y = choice([-5, 5])
        self.rect = (self.image.get_rect())
        self.rect.x = x
        self.rect.y = y
    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_one(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WH - PLAYER2_HEIGHT:
            self.rect.y += self.speed
    

class Player_two(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WH - PLAYER2_HEIGHT:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global score1, score2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= WH - BALL_SIZE:
            self.speed_y *= -1
        if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            self.speed_x *= -1
    def reset(self):
        self.speed_x = choice([-5, 5])
        self.speed_y = choice([-5, 5])
        self.rect.x = WW / 2 - BALL_SIZE / 2
        self.rect.y = WH / 2 - BALL_SIZE / 2

WW, WH = 1120, 700
PLAYER1_WIDTH = 10
PLAYER1_HEIGHT = 120
PLAYER2_WIDTH = 10
PLAYER2_HEIGHT = 120
BALL_SIZE = 15
BLUE = (0, 80, 255)
game = True
finish = False
max_score = 9
score1 = 0
score2 = 0
text = " "

window = display.set_mode((WW, WH))
player1 = Player_one("rocketka (1).png", 10, WH / 2 - PLAYER1_HEIGHT / 2, PLAYER1_WIDTH, PLAYER1_HEIGHT, 10)
player2 = Player_two("rocketka (1).png", WW - (PLAYER2_WIDTH + 10), WH / 2 - PLAYER2_HEIGHT / 2, PLAYER2_WIDTH, PLAYER2_HEIGHT, 10)
ball = Ball("ball (1).png", WW / 2 - BALL_SIZE / 2, WH / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE, 0)

font.init()
my_font1 = font.Font(None, 36)
my_font2 = font.Font(None, 72)
score_text = my_font1.render(f"{score1}:{score2}", True, (255, 255, 255))
win_text = my_font2.render(text, True, (255, 255, 255))

FPS = 60
clock = time.Clock()

while game:
    WW, WH = window.get_size()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(BLUE)
        player1.update()
        player2.update()
        player1.draw_sprite()
        player2.draw_sprite()
        ball.update()
        ball.draw_sprite()
        if ball.rect.x <= 15 or ball.rect.x >= WW - 30:
            if ball.rect.x <= 15:
                score2 += 1
            else:
                score1 += 1
            ball.reset()
        score_text = my_font1.render(f"{score1}:{score2}", True, (255, 255, 255))
        window.blit(score_text, (WW / 2 - score_text.get_width(), 14))
        if score1 == max_score or score2 == max_score:
            if score1 == max_score:
                text = "Игрок 1 победил!"
            else:
                text = "Игрок 2 победил!"
            win_text = my_font2.render(text, True, (255, 255, 255))
            window.blit(win_text, (WW / 2 - win_text.get_width(), WH / 2 - win_text.get_height()))
            finish = True
    clock.tick(FPS)
    display.flip()
