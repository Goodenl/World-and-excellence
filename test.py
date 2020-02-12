import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("LOL TEST!")

x = 50
y = 50
width = 30
hieght = 60
vel = 5

run = True

# main loop
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # register key pressed
    keys = pygame.key.get_pressed()
    # check need button
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, hieght))
    pygame.display.update()

pygame.quit()
