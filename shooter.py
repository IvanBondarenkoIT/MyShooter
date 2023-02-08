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


class Bullet(GameSprite):
    """Bullet Class"""
    pass


class Statistics:
    pass


def save_statistic(filename):
    pass

