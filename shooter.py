import pygame
from pygame import *
from setting import *
from random import randint
import time


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        """This is method init()"""
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        pass
        # window.blit(self.image, (self.rect.x, self.rect.y))  # : add obj


class Player(GameSprite):
    """Player Class"""
    def update(self) -> None:
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIN_WIDTH - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(IMG_BULLET, self.rect.centerx, self.rect.top, 15, 20, -15)
        # bullets.add(bullet)  # : add seq


class Enemy(GameSprite):
    """Enemy Class"""
    def update(self) -> None:
        self.rect.x += self.speed
        global LOST
        if self.rect.y > WIN_HEIGHT:
            self.rect.x = randint(80, WIN_WIDTH - 80)
            self.rect.y = 0
            LOST += 1


class Bullet(GameSprite):
    """Bullet Class"""
    def update(self) -> None:
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class Statistics:
    def __init__(self, st_point_win=0, st_point_lose=0, duration=0, level=0):
        self._st_point_win = st_point_win
        self._st_point_lose = st_point_lose
        self._duration = duration
        self._level = level

    def __repr__(self):
        return f'{self._st_point_win} {self._st_point_lose} {self._duration} {self._level}'


def save_statistic(filename):
    pass


font.init()
font1 = font.Font(None, 80)
win = font1.render(WIN_TEXT, True, WIN_COLOR)
lose = font1.render(LOSE_TEXT, True, LOSE_COLOR)

mixer.init()
mixer.music.load(MAIN_MUSIC_PATH)
mixer.music.play(-1)
mixer.music.set_volume(0.01)
fire_sound = mixer.Sound(EFFECTS_MUSIC_PATH)
fire_sound.set_volume(0.01)


# create window
display.set_icon(image.load(ICON))
display.set_caption(WIN_TITLE)
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
background = transform.scale(image.load(IMG_BACK), (WIN_WIDTH, WIN_HEIGHT))
timer = time.time()
# create sprites
ship = Player(IMG_HERO, 5, WIN_HEIGHT - 100, 80, 100, 10)
monsters = sprite.Group
for i in range(1, 6):
    monster = Enemy(IMG_ENEMY, randint(80, WIN_WIDTH - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()

stat = []

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            fire_sound.play()
            ship.fire()

        if LEVEL < 1:
            run = False

        if not finish:
            window.blit(background, (0, 0))

            ship.update()
            monsters.update()
            bullets.update()

            ship.reset()
            monster.draw(window)
            bullets.draw(window)

            if LEVEL == 3:
                for c in collides:
                    SCORE += 1
                    monster = Enemy(IMG_ENEMY, randint(80, (WIN_WIDTH - 80),
                                                       -40, 80, 50, randint(1, 7)))
                    monsters.add(monster)

            collides = sprite.groupcollide(monsters, bullets, True, True)

            for c in collides:
                SCORE += 1
                monster = Enemy(IMG_ENEMY, randint(80, (WIN_WIDTH - 80),
                                                   -40, 80, 50, randint(1, 7)))
                monsters.add(monster)

            if sprite.spritecollide(ship, monsters, False) or LOST >= MAX_LOST:
                finish = True
                window.blit(win, (200, 200))

            # lebel_win =


