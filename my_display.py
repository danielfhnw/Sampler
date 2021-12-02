import pygame

def set_display():
    pygame.init()
    pygame.display.set_caption('Sampler by DJ&G')
    bg = pygame.display.set_mode([1280,720])
    image = pygame.image.load('/home/pi/Sampler/djbooth.jpg')
    bg.blit(image, [0,0])
    pygame.display.update()
    
def quit_display():
    pygame.quit()