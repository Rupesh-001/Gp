import pygame

pygame.init()

white = (255, 255, 255)
height = 400
width = 400

display_surface = pygame.display.set_mode((height, width))
pygame.display.set_caption('Image')

image = pygame.image.load("C:\\Users\\ASUS1\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-10-18 171338.png")

while True:
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
