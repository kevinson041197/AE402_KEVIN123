import pygame
PINK =pygame.color.Color("#FF87EE")
pygame.init()

size = (700, 500)
screen =plgame.display.set_mode(size)
pygame.display.set_caption("pink screen")

done = False
clock =pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        for e