import pygame

pygame.init()
size = (400, 600)

screen =  pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit")
            pygame.quit()
            exit(0)