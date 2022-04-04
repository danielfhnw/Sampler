import pygame
import my_mixer as mx

def set_display():
    pygame.init()
    pygame.display.set_caption('Sampler by DJ&G')
    screen = pygame.display.set_mode([1920,1080])
    update()

def update():
    screen = pygame.display.get_surface()
    screen.fill((0,0,0))
    image = pygame.image.load('/home/pi/Sampler/djbooth.jpg')
    screen.blit(image, (0,0))
    font = pygame.font.Font('freesansbold.ttf', 32)
    txt_vol = font.render("Volume: " + str(mx.get_vol()), True, (255,255,255))
    screen.blit(txt_vol, (50,750))
    page = mx.get_page()
    txt_page = font.render("Page: " + str(page), True, (255,255,255))
    screen.blit(txt_page, (300,750))
    txt_sounds = font.render("Name:", True, (255,255,255))
    screen.blit(txt_sounds, (1400,50))
    txt_sounds2 = font.render("Vol:", True, (255,255,255))
    screen.blit(txt_sounds2, (1800,50))
    sounds = mx.get_sounds()
    for i in range(9):
        try:
            txt = font.render(str(i) + ":   " + str(sounds[i+page*10][0]), True, (255,255,255))
            txt2 = font.render(str(sounds[i+page*10][1]), True, (255,255,255))
            screen.blit(txt, (1350,i*50+100))
            screen.blit(txt2, (1800,i*50+100))
        except:
            pass
    pygame.display.update()

def quit_display():
    pygame.quit()
