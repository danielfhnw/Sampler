# Sampler by DJ & G
# contact DJ for software support or expansion ideas

# import
import pygame
import subprocess
import my_mixer as mx
import my_display as dp

shutdown = 0;

dp.set_display()

mx.init_mixer()

dp.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dp.quit_display()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP0:
                mx.play(0)
            if event.key == pygame.K_KP1:
                mx.play(1)
            if event.key == pygame.K_KP2:
                mx.play(2)
            if event.key == pygame.K_KP3:
                mx.play(3)
            if event.key == pygame.K_KP4:
                mx.play(4)
            if event.key == pygame.K_KP5:
                mx.play(5)
            if event.key == pygame.K_KP6:
                mx.play(6)
            if event.key == pygame.K_KP7:
                mx.play(7)
            if event.key == pygame.K_KP8:
                mx.play(8)
            if event.key == pygame.K_KP9:
                mx.play(9)
            if event.key == pygame.K_KP_PERIOD:
                mx.stop()
            if event.key == pygame.K_KP_DIVIDE:
                mx.page_down()
                dp.update()
            if event.key == pygame.K_KP_MULTIPLY:
                mx.page_up()
                dp.update()
            if event.key == pygame.K_KP_MINUS:
                mx.vol_down()
                dp.update()
            if event.key == pygame.K_KP_PLUS:
                mx.vol_up()
                dp.update()
            if event.key == pygame.K_KP_ENTER:
                mx.pause()
            if event.key == pygame.K_BACKSPACE:
                mx.hello()
            if event.key == pygame.K_NUMLOCK:
                shutdown = shutdown + 1
                if shutdown > 2:
                    mx.quit_mixer()
                    dp.quit_display()
                    subprocess.call(['shutdown', '-h', 'now'])
            else:
                shutdown = 0
