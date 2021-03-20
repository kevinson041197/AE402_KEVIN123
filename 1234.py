import pygame


pygame.init()
size = (400,400)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('下雪')
snow_list = []

for i in range(50):
    x = random.randrange(0,400)
    y = random.randrange(0,400)
done = False

clock = pygame.time.Clock()
        for i in