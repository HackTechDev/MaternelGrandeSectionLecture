# -*- coding: utf-8 -*-
import pygame
import random
import sys
import os
import webbrowser
import time
import sqlite3 as lite
import subprocess

sys.path.append('./package')

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

def main():

    pygame.init()

    screen_width = 1024
    screen_height = 768
    screen=pygame.display.set_mode([screen_width,screen_height])

    font = pygame.font.Font(None, 25)

    pygame.display.set_caption("Ecouter les mots")

    done = False

    clock=pygame.time.Clock()

    file = open("fruit/fruit.list", "r")
    line_list = file.readlines()
    file.close()

    fruit_list = []

    for line in line_list:
        line = line[:-1]
        fruit_list.append(line)

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    numberFruit = random.randint(1, len(fruit_list)) - 1
                    cmd = "mplayer fruit/" + fruit_list[numberFruit] + ".wav"
                    status = os.popen(cmd)                   

        screen.fill(white)

        gameText = font.render("Ecouter les mots", True, ( 255, 0, 0))
        screen.blit(gameText, [10, 10])
        
        infoText = font.render(u"Appuyer sur la touche [Espace] pour écouter un nouveau mot", True, ( 255, 0, 0))
        screen.blit(infoText, [10, 30])
 
        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

if __name__ == "__main__":
    main()
