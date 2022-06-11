# start of imports
import pygame
import time
import sys
import os
os.system('pip install pygame')
import random
import tkinter as tk
import os
import random
# end of imports
print("Initalizing Tool...")
time.sleep(1)
print("Initalized Succesfully!")
time.sleep(1)
print("Importing Proxies")
time.sleep(1)
print("Proxies Imported Succesfully!")
time.sleep(1)
print("Contacting Host For Connection...")
time.sleep(1)
print("Success, Connected to host 127.0.0.1")
time.sleep(1)
IP = input("Please input the IP you wish to hit offline: ")
time.sleep(1)
print("Hitting", IP, "offline please wait.....")
# cool epic pygame vars
pygame.init()
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((620, 500))
black = pygame.image.load('B1.png')
white = pygame.image.load('B2.png')
pygame.mixer.music.load('idiot.mp3')
clock = pygame.time.Clock()


def gamerloop():
    screen.blit(black, (0, 0))
    pygame.display.update()
    screen.blit(white, (0, 0))


# end of vars
pygame.display.set_caption('You are an Idiot!')
screen.fill(background_colour)
pygame.display.flip()
pygame.mixer.music.play(-1)


running = True
while running:
    pygame.display.flip()
    screen.blit(white, (0, 0))
    pygame.time.delay(890)
    pygame.display.flip()
    screen.blit(black, (0, 0))
    pygame.time.delay(890)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
# Main Problem {
# my main problem is that I cannot move the screen
# I have tried to do so with pygame.display.set_mode and making the x/y random variables
# however that only changed the length and the width of the window not where it was located at on the screen
# I Think in order to resolve my problem I need to somehow change the window not the resolution of the screen
# something like pygame.window(x,y) in order to move it around
# Side Problem (If main problem gets fixed)
# Can't figure out way for script to duplicate smaller windows after window is close or figure out
# how the script is gonna start itself again after getting closed by. }
