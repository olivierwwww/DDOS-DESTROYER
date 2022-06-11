# start of imports
import os
os.system('pip install pygame')
import pygame
import time
import sys
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
pygame.mixer.music.load('redspider.mp3
clock = pygame.time.Clock()
def gamerloop():
    screen.blit(black, (0,0))
    pygame.display.update()
    screen.blit(white, (0,0))
    
# end of vars
pygame.display.set_caption('You are an Idiot!')
screen.fill(background_colour)
pygame.display.flip()
pygame.mixer.music.play(-1)


running = True
while running:
    pygame.display.flip()
    screen.blit(white, (0,0))
    pygame.time.delay(890)
    pygame.display.flip()
    screen.blit(black, (0,0))
    pygame.time.delay(890)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

