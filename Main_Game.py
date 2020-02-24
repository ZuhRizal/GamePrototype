""" Code source by freeCodeCamp.org """

import pygame
import math
import random

pygame.init()

# Game screen
screen = pygame.display.set_mode((800, 600))
backgroud = pygame.image.load("Space.jpg")

# score
jumlah_score = 0
jenis_font = pygame.font.Font("freesansbold.ttf", 32)
fontkoordinatX = 10
fontkoordinatY = 10


def tampilan_score(x, y):
    score = jenis_font.render("Score : " + str(jumlah_score), True, (225, 225, 225))
    screen.blit(score, (x, y))


# Game over
over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over_teks():
    over_teks = over_font.render("GAME OVER", True, (225, 225, 225))
    screen.blit(over_teks, (200, 250))


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


# Bullet
bullet = pygame.image.load("bullet.png")
bullet = pygame.transform.scale(bullet, (20, 20))
bulletkoordinatX = 0
bulletkoordinatY = 430
bulletX_change = 0
bulletY_change = 10
keadaan_bullet = "ready"


def fire_bullet(x, y):
    global keadaan_bullet
    keadaan_bullet = "fire"
    screen.blit(bullet, (x + 6, y + 10))


# Enemies
enemy = []
invaders = []
musuhX = []
musuhY = []
musuhX_change = []
musuhY_change = []
jumlah_musuh = 20

for i in range(jumlah_musuh):
    enemy.append(pygame.image.load("Space Alien Transparan.png"))
    musuhX.append(random.randint(10, 753))
    musuhY.append(random.randint(10, 118))
    musuhX_change.append(2)
    musuhY_change.append(20)


def musuh(x, y, alien):
    screen.blit(enemy[alien], (x, y))


# Reaksi
def isCollision(musuhkoordinatX, musuhkoordinatY, bulletkoordinatX, bulletkoordinatY):
    jarak = math.sqrt(
        (math.pow(musuhkoordinatX - bulletkoordinatX, 2)) + (math.pow(musuhkoordinatY - bulletkoordinatY, 2)))
    if jarak <= 27:
        return True
    else:
        return False


# Game loop atau jalannya game
running = True
while running:

    # RGB : Red Green Blue
    screen.fill((0, 0, 0))

    # Background
    screen.blit(backgroud, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pergerakan pesaawat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_UP:
                playerY_change = -3
            if event.key == pygame.K_DOWN:
                playerY_change = 3
            if event.key == pygame.K_SPACE:
                if keadaan_bullet is "ready":
                    bulletkoordinatX = playerkoordinatX
                    fire_bullet(bulletkoordinatX, bulletkoordinatY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Pergerakan dan batasan frame karakter
    playerkoordinatX += playerX_change

    if playerkoordinatX <= 5:
        playerkoordinatX = 5
    elif playerkoordinatX >= 763:
        playerkoordinatX = 763

    playerkoordinatY += playerY_change

    if playerkoordinatY <= 10:
        playerkoordinatY = 10
    elif playerkoordinatY >= 558:
        playerkoordinatY = 558

    # Tembakan peluru
    if bulletkoordinatY <= 0:
        bulletkoordinatY = playerkoordinatY
        keadaan_bullet = "ready"

    if keadaan_bullet is "fire":
        fire_bullet(bulletkoordinatX, bulletkoordinatY)
        bulletkoordinatY -= bulletY_change

    # Pergerakan dan batasan musuh
    for i in range(jumlah_musuh):

        musuhX[i] += musuhX_change[i]
        if musuhX[i] <= 10:
            musuhX_change[i] = 2
            musuhY[i] += musuhY_change[i]
        elif musuhX[i] >= 753:
            musuhX_change[i] = -2
            musuhY[i] += musuhY_change[i]


        # Collision
        collision = isCollision(musuhX[i], musuhY[i], bulletkoordinatX, bulletkoordinatY)
        if collision:
            bulletkoordinatY = playerkoordinatY
            keadaan_bullet = "ready"
            jumlah_score += 1
            musuhX[i] = random.randint(10, 753)
            musuhY[i] = random.randint(10, 418)

        musuh(musuhX[i], musuhY[i], i)

        # Game over
        if musuhY[i] > 500:
            for j in range(jumlah_musuh):
                musuhY[j] = 2000
            game_over_teks()
            break

    tampilan_score(fontkoordinatX, fontkoordinatY)
    player(playerkoordinatX, playerkoordinatY)
    pygame.display.update()
