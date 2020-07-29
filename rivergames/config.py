import pygame
import random
import math

#initializing pygame
pygame.init()

#initializing values 
player = 1
level = 1
x = 0
boat_index = 0
lost = None
winners = []
count = 0
player1 = 0 
player2 = 0
draw = 0 
timer_started = False
timer_started1 = False
clock = pygame.time.Clock()

#initializing fonts
font = pygame.font.Font(None, 40)
font1 = pygame.font.SysFont('Algerian',30)
font2 = pygame.font.SysFont('Algerian',28)
font_level = pygame.font.SysFont('Brush Script MT',66)
font_player = pygame.font.SysFont('Brush Script MT',40)
font_color = pygame.Color('red')
font_color1 = pygame.Color('blue')
font_color2 = pygame.Color('black')
font_color3 = pygame.Color('white')

#intializing screen size
root = pygame.display.set_mode((870,680))

#importing required images
icon = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\icon.png")
background = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\backround.jpg")
win = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\win.jpg")
player1_image = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\player1.png")
player2_image = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\player2.png")
start = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\start.jpg")
arrow = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\arrow.png")
arrowk = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\arrow-key.png")
skull = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\danger.png")
enemy = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\enemy.png")
final = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\back.jpg")

#Initializing player position 
player1_x = 450
player1_y = 650
player1_xchange = 0
player1_ychange = 0 
player2_x = 450
player2_y = 50
player2_xchange = 0
player2_ychange = 0
pygame.display.set_icon(icon)

#Intializing obstacle position
rock_image = []
stone_image=[]
stone_x = []
rock_x = []
stone1_x = []
rock1_x = []
#Initializing obstacles positions
stone_y = [510, 390, 270, 150]
rock_y = [520, 400, 280, 160]
boat_y = [580, 460, 340, 220, 100, 580, 460, 340, 220, 100]
skull_x=[25, 390, 200, 770, 25, 390, 200, 770]
skull_y=[540, 540, 420, 420, 300, 300, 180, 180]
enemy_y=[540, 420, 300, 180]
enemy_x=[25, 200, 25, 200]


for i in range(0, 4) :
    stone_image.append(pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\cave.png"))
    rock_image.append(pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\stone.png"))
    stone_x.append(random.randint(50, 150))
    rock_x.append(random.randint(230, 300))
    stone1_x.append(random.randint(600, 630))
    rock1_x.append(random.randint(450, 550))
boat_image = []
boat_x = []
for i in range(0, 10) :
    boat_image.append(pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\ship.png"))
    if boat_index < 5 :
        boat_x.append(random.randint(0, 400))
        boat_index+=1
    if boat_index in range(4, 10) :
        boat_x.append(random.randint(450, 800))
        boat_index+=1

#This function displays the player 1
def dispplayer1(x, y) :
    grass1=pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\grass.jpg")
    root.blit(grass1, (0, 650))
    root.blit(player1_image, (x, y))

#This function displays the grass
def dispgrass(i, grass_list) :
    grass = pygame.image.load(r"C:\Users\DELL\github\pygames\rivergames\grass.jpg")
    root.blit(grass, (0, grass_list[i]))