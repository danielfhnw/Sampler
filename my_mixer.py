import pygame
import csv
import math

sounds = []                             # {{soundpath_0 , volume_0}.....}
sound_path = '/media/pi/SAMPLER/'       # path to soundfolder
page = 0                                # page mapping for the keys 0..len(sounds)/10
paused = False                          # mixer paused or not
master_vol = 5                          # master volume 0..10

def play(i):
    try:
        channel = pygame.mixer.find_channel(True)
        sound_config = sounds[i+page*10]
        sound = pygame.mixer.Sound(sound_path + sound_config[0])
        sound.set_volume(sound_config[1]*master_vol/10)
        channel.play(sound)
        print('Sampler is playing: ' + sound_config[0])
    except IndexError:
        print('Key not set')
    except:
        print('File not found or in the wrong format')

def pause():
    global paused
    if not paused:
        pygame.mixer.pause()
        paused = True
        print('Sampler is paused')
    else:
        pygame.mixer.unpause()
        paused = False
        print('Sampler is unpaused')

def stop():
    pygame.mixer.fadeout(500)
    print('Sampler is stopped')

def vol_up():
    global master_vol
    if master_vol < 10:
        master_vol += 1
        print('Master Volume is set to: ' + str(master_vol))

def vol_down():
    global master_vol
    if master_vol > 0:
        master_vol -= 1
        print('Master Volume is set to: ' + str(master_vol))

def get_vol():
    global master_vol
    return master_vol

def page_up():
    global page
    if page < math.floor(len(sounds)/10):
        page += 1
        print('Key-Mapping Page is set to: ' + str(page))

def page_down():
    global page
    if page > 0:
        page -= 1
        print('Key-Mapping Page is set to: ' + str(page))

def get_page():
    global page
    return page

def get_sounds():
    global sounds
    return sounds

def hello():
    try:
        channel = pygame.mixer.find_channel(True)
        sound = pygame.mixer.Sound('/home/pi/Sampler/helloMotherfucker.wav')
        channel.play(sound)
        print('Hello Motherfucker!')
        if paused:
            print('Sampler is paused')
        else:
            print('Sampler is unpaused')
        print('Master Volume is set to: ' + str(master_vol))
        print('Soundpath is: ' + sound_path)
        print('Key-Mapping Page is set to: ' + str(page))
    except:
        print('Something is wrong')

def init_mixer():
    pygame.mixer.init()
    try:
        with open('/media/pi/SAMPLER/SamplerConfig.csv', newline='') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                sounds.append([row['Sound'], float(row['Volume'])])
        hello()   
    except:
        print('Sampler could not be initialized')
        try:
            channel = pygame.mixer.find_channel(True)
            sound = pygame.mixer.Sound('/home/pi/Sampler/oh-shit.wav')
            channel.play(sound)
        except:
            print('Something is very wrong')
            
def quit_mixer():
    try:
        channel = pygame.mixer.find_channel(True)
        sound = pygame.mixer.Sound('/home/pi/Sampler/shutdown.wav')
        channel.play(sound)
        while channel.get_busy():
            master_vol = 5              # wait for shutdown sound to finish
        print('Goodbye!')
    except:
        print('Something is wrong')
