__author__ = "ZuhRizal"

import pygame
import random

pygame.init()

# Game screen
screen = pygame.display.set_mode((800, 600))

# Judul dan logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Hologram effect 2.png")
pygame.display.set_icon(icon)

# Character
character = pygame.image.load("Pesawat.png")
playerkoordinatX = 355
playerkoordinatY = 430
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(character, (x, y))


# Enemies
enemy = pygame.image.load("Musuh.png")
musuhkoordinatX = random.randint(10, 345)
musuhkoordinatY = random.randint(10, 205)
musuhX_change = 0.5
musuhY_change = 20


def musuh(x, y):
    screen.blit(enemy, (x, y))


# Game loop atau jalannya game
running = True
while running:

    # RGB : Red Green Blue
    screen.fill((100, 0, 180))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pergerakan pesaawat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerkoordinatX += playerX_change

    if playerkoordinatX <= 5:
        playerkoordinatX = 5
    elif playerkoordinatX >= 683:
        playerkoordinatX = 683

    playerkoordinatY += playerY_change

    if playerkoordinatY <= 10:
        playerkoordinatY = 10
    elif playerkoordinatY >= 438:
        playerkoordinatY = 438

    # Pergerakan musuh
    musuhkoordinatX += musuhX_change

    if musuhkoordinatX <= 10:
        musuhX_change = 0.5
        musuhkoordinatY += musuhY_change
    elif musuhkoordinatX >= 678:
        musuhX_change = -0.5
        musuhkoordinatY += musuhY_change

    player(playerkoordinatX, playerkoordinatY)
    musuh(musuhkoordinatX, musuhkoordinatY)
    pygame.display.update()
