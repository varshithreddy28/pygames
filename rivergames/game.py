#importing modules
import pygame
import random
import math
from config import *

#initializing pygame
pygame.init()


#This function displays the player 2
def dispplayer2(x, y) :
    root.blit(player2_image, (player2_x, player2_y))

#This function displays Backround
def dispbackgroung() :
    root.blit(background,(0, 0))
grass_list = [530, 410, 290, 170, 50]

#This are used to display the obstacles
def dispship(x, y, i) :
    root.blit(boat_image[i], (boat_x[i], boat_y[i]))
def dispstone(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, i) :
    root.blit(stone_image[i], (stone_x[i], stone_y[i]))
    root.blit(rock_image[i], (rock_x[i], rock_y[i]))
    root.blit(stone_image[i], (stone1_x[i], stone_y[i]))
    root.blit(rock_image[i], (rock1_x[i], rock_y[i]))

#This function will append the winners
def appending(lost, score, score1) :
    global winners, passed_time, passed_time1
    if score == score1:
        if  passed_time>passed_time1 :
            winners.append('player2')
        elif passed_time<passed_time1:
            winners.append('player1')
        elif passed_time == passed_time1:
            winners.append('draw')
    elif lost == 'player1':
        if score == score1 :
            if  passed_time > passed_time1 :
                winners.append('player2')
            elif passed_time < passed_time1 :
                winners.append('player1')
            elif passed_time == passed_time1 :
                winners.append('draw')
        if score<score1 :
            winners.append('player2')
        elif score1 == 70 :
            winners.append('player2')
        if score > score1 :
            winners.append('player1')
    elif lost =='player2':
        if score == score1 :
            if  passed_time > passed_time1 :
                winners.append('player2')
            elif passed_time < passed_time1 :
                winners.append('player1')
            elif passed_time == passed_time1 :
                winners.append('draw')
        if score>score1:
            winners.append('player1')
        elif score == 70 :
            winners.append('player1')
        if score < score1 :
            winners.append('player2')

#This function will calculate the score               
def calculatescore(boat_y, grass_list, player1_y, player2_y) :
    global index, score, score1, index1, index3, index4, winners
    if index<=4 :
        if boat_y[index]>=player1_y :
            score+=10
            index+=1 
    if index1 < 4 :    
        if grass_list[index1]>=player1_y :      
            score+=5
            index1+=1
    if index3>=0 :
        if boat_y[index3]<=player2_y:
            score1+=10
            index3-=1
    if index4>0 :    
        if grass_list[index4-1]<=player2_y :      
            score1+=5
            index4-=1

#This function will check collision between players and obstacles
def collide_rock(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, player2_x, player2_y) :
    global gamestart, timer_started, timer_started1, level, lost, score, score1, player
    stone_x1 = stone_x[i]+18
    stone_y1 = stone_y[i]+32
    stone1_x1 = stone1_x[i]+18
    stone1_y1 = stone_y[i]+32
    rock_x1 = rock_x[i]+18
    rock_y1 = rock_y[i]+28
    rock1_x1 = rock1_x[i]+18
    rock1_y1 = rock_y[i]+28
    distance_stone = math.sqrt(pow((stone_x1-player1_x), 2)+(pow((stone_y1-player1_y), 2)))
    distance_rock = math.sqrt(pow((rock_x1-player1_x), 2)+(pow((rock_y1-player1_y), 2)))
    distance_stone1 = math.sqrt(pow((stone1_x1-player1_x), 2)+(pow((stone_y1-player1_y), 2)))
    distance_rock1 = math.sqrt(pow((rock1_x1-player1_x), 2)+(pow((rock1_y1-player1_y), 2)))
    distance1_stone = math.sqrt(pow((stone_x1-player2_x), 2)+(pow((stone_y1-player2_y), 2)))
    distance1_rock = math.sqrt(pow((rock_x1-player2_x), 2)+(pow((rock_y1-player2_y), 2)))
    distance1_stone1 = math.sqrt(pow((stone1_x1-player2_x), 2)+(pow((stone_y1-player2_y), 2)))
    distance1_rock1 = math.sqrt(pow((rock1_x1-player2_x), 2)+(pow((rock1_y1-player2_y), 2)))
    if player == 1 :
        if distance_rock < 40 :
            player+=1
            lost = 'player1'
            return True
        if distance_stone < 50 :
            player+=1
            lost = 'player1'
            return True
        if distance_rock1 < 40 :
            player+=1
            lost = 'player1'
            return True
        if distance_stone1 < 50 :
            player+=1
            lost = 'player1'
            return True
    if player == 2 :
        if distance1_rock < 40:
            player+=1
            lost = 'player2'
            appending(lost, score, score1)
            gamestart = False        
            return True
        if distance1_stone < 50:
            player+=1
            lost = 'player2'
            appending(lost, score, score1)
            gamestart = False
            return True
        if distance1_rock1 < 40 :
            player+=1
            lost = 'player2'
            appending(lost, score, score1)
            gamestart = False
            return True
        if distance1_stone1 < 50:
            player+=1
            lost = 'player2'
            appending(lost, score, score1)
            gamestart = False
            return True
def collide_boat(boat_x, boat_y, i) :
    global level, gamestart, lost, player
    boat_x1 = boat_x[i]+18
    boat_y1 = boat_y[i]+32
    distance_boat = math.sqrt(pow((boat_x1-player1_x), 2)+(pow((boat_y1-player1_y), 2)))
    distance1_boat = math.sqrt(pow((boat_x1-player2_x), 2)+(pow((boat_y1-player2_y), 2)))
    if player == 1 :
        if distance_boat < 30 :
            player+=1
            lost = 'player1'
            return True
    if player == 2 :
        if  distance1_boat < 30 :
            player+=1
            lost = 'player2'
            appending(lost, score, score1)
            gamestart = False        
            return True

#This function will Display score and time
def timer(score, score1, passed_time, passed_time1):
    text1 = font.render("Time: "+str(passed_time/1000), True, font_color)
    root.blit(text1, (10, 50))
    text2 = font.render("Time: "+str(passed_time1/1000), True, font_color)
    root.blit(text2, (650, 50))
    score_font = font.render("Score: "+str(score), True, font_color)
    root.blit(score_font, (10, 20))
    score1_font = font.render("Score: "+str(score1), True, font_color)
    root.blit(score1_font, (650, 20))

#This function will displays the instructions on the start screen
def dispstart() :
    root.blit(start, (0, 0))
    root.blit(arrow, (730, 310))
    root.blit(arrowk, (15, 310))
    text = font2.render("3.This game consists of 5 levels ", True, font_color2)
    text1 = font_level.render("Controls : ", True, font_color2)
    text2 = font_player.render("Player 2 : ", True, font_color2)
    text3 = font_player.render("Player 1 : ", True, font_color2)
    text4 = font_level.render("Press Enter to Start", True, font_color2)
    root.blit(player2_image, (40, 490))
    root.blit(player1_image, (760, 490))
    root.blit(text, (12, 130))
    root.blit(text1, (6, 275))
    root.blit(text2, (15, 440))
    root.blit(text3, (730, 440))
    root.blit(text4, (200, 500))

#This function's will check the winners
def checkwinner1(player1_y, player2_y, score, score1, passed_timer, passed_timer1):
    global timer_started, timer_started1, level, lost, gamestart, player
    if score == 70 :
        timer_started = False
        timer_started1 = True
        lost = 'player2'
        player+=1
    elif player1_y<=50 :
        timer_started = False
        timer_started1 = True
        lost = 'player2'
        player+=1
def checkwinner2(player1_y, player2_y, score, score1, passed_timer, passed_timer1) :
    global timer_started, timer_started1, level, lost, gamestart, player
    if score1 == 70 :
        timer_started = False
        timer_started1 = False
        lost = 'player1'
        player+=1
        appending(lost, score, score1)
        gamestart = False
    elif player2_y>=650 :
        timer_started = False
        timer_started1 = False
        lost = 'player1'
        player+=1
        appending(lost, score, score1)
        gamestart = False  

#This function will display the winner's and scores   
def gameover(winner, score, time, loss, score1, time1, level):
    root.blit(win, (0, 0))
    text = font1.render("Winner : "+winner, True, font_color1)  
    root.blit(text ,(180, 350))
    text1 = font1.render("Score : "+str(score), True, font_color1)  
    root.blit(text1, (350, 380)) 
    text2 = font1.render("Time : "+str(time/1000), True, font_color1)  
    root.blit(text2, (350, 410))      
    text3 = font1.render(loss, True, font_color1)  
    root.blit(text3, (300, 440))
    text4 = font1.render("Score : "+str(score1), True, font_color1)  
    root.blit(text4,(350,470)) 
    text5 = font1.render("Time : "+str(time1/1000), True, font_color1)  
    root.blit(text5 ,(350, 500))    
    text6=font_level.render("Level "+str(level), True, font_color2)
    root.blit(text6, (380, 50))
    text7=font_level.render("Press Enter to Continue...", True, font_color2)
    root.blit(text7, (200, 580))

#This will display the obstacles
def  danger(skull_x, skull_y, i) :
    root.blit(skull, (skull_x[i], skull_y[i]))
enemy_xchange = 12
def dispenemy(enemy_x, enemy_y, i) :
    root.blit(enemy, (enemy_x[i], enemy_y[i]))

#This will check the collision with the obtsacles
def collide_skull(skull_x, skull_y) :
    global gamestart, lost, score, score1, player1_x, player1_y, player2_x, player2_x
    skull_x1 = skull_x[i]-5
    skull_y1 = skull_y[i]+5
    distance_skull = math.sqrt(pow((skull_x1-player1_x), 2)+(pow((skull_y1-player1_y), 2)))
    distance1_skull = math.sqrt(pow((skull_x1-player2_x), 2)+(pow((skull_y1-player2_y), 2)))
    if distance_skull < 20 :        
        score-=5
        player1_x = player1_x+15
    if  distance1_skull < 20 :
        score1-=5
        player2_x+=15 

def collide_enemy(enemy_x, enemy_y) :
    global gamestart, lost, score, score1, player1_x, player1_y, player2_x, player2_y
    enemy_x1 = enemy_x
    enemy_y1 = enemy_y
    distance_enemy = math.sqrt(pow((enemy_x1-player1_x), 2)+(pow((enemy_y1-player1_y), 2)))
    distance1_enemy = math.sqrt(pow((enemy_x1-player2_x), 2)+(pow((enemy_y1-player2_y), 2)))
    if distance_enemy < 20 :        
        score-=4
        player1_x = 450
        player1_y = 650
    if  distance1_enemy < 20 :
        score1-=4
        player2_x = 450
        player2_y = 50

#this functions will Display the scores
def scores(winners) :
    global count, player1, player2, draw
    root.blit(final, (0, 0))
    if count == 0 :
        for i in winners :
            if i == 'player1' :
                player1+=1
            elif i == 'player2' :
                player2+=1
            elif i == 'draw' :
                draw+=1
        count+=1
    text=font2.render("Player 1 : "+str(player1), True, font_color3)
    text1=font2.render("Player 2 : "+str(player2), True, font_color3)
    text2=font2.render("Draw : "+str(draw), True, font_color3)
    root.blit(text, (300, 200))
    root.blit(text1, (300, 300))
    root.blit(text2, (400, 400))  
pygame.display.set_caption('rivercrossing')
running = True
player = True
passed_time = 0
passed_time1 = 0
gamestart = False

#Initializing Game loop
while running:
    root.fill((0, 0, 0))
    dispbackgroung()
    for i in range(0, 5) :
        dispgrass(i, grass_list)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    if gamestart :
        dispbackgroung()
        for i in range(0, 5) :
            dispgrass(i, grass_list)
        
        #Checks if any key is pressed
        if event.type == pygame.KEYDOWN :
            #Controlls for player 1  and their speed
            if player == 1 :
                if event.key == pygame.K_LEFT :
                    player1_xchange-=5
                if event.key == pygame.K_RIGHT :
                    player1_xchange+=5
                if event.key == pygame.K_UP :
                    player1_ychange-=5
                if event.key == pygame.K_DOWN :
                    player1_ychange+=5
                if event.key == pygame.K_SPACE :
                    player1_ychange-=10
            #Controlls for player 2 and their speed        
            if player==2 : 
                if event.key == pygame.K_a :
                    player2_xchange-=5
                if event.key == pygame.K_d :
                    player2_xchange+=5
                if event.key == pygame.K_w :
                    player2_ychange-=5
                if event.key == pygame.K_s :
                    player2_ychange+=5
                if event.key == pygame.K_SPACE :
                    player2_ychange-=10
        
        #Checks if any key is released
        if event.type == pygame.KEYUP :
            if player == 1 :
                if event.key == pygame.K_LEFT :
                    player1_xchange = 0
                if event.key == pygame.K_RIGHT :
                    player1_xchange = 0
                if event.key == pygame.K_UP :
                    player1_ychange = 0
                if event.key == pygame.K_DOWN :
                    player1_ychange = 0
                if event.key == pygame.K_SPACE :
                    player1_ychange = 0
            if player==2 :
                if event.key == pygame.K_a :
                    player2_xchange = 0
                if event.key == pygame.K_d :
                    player2_xchange = 0
                if event.key == pygame.K_w :
                    player2_ychange = 0
                if event.key == pygame.K_s :
                    player2_ychange = 0
                if event.key == pygame.K_SPACE :
                    player2_ychange = 0
        
        #Modifys player1 position
        player1_x+=player1_xchange
        player1_y+=player1_ychange

        #Modifiying player1 boundaries
        if player1_x>=860 :
            player1_x = 860
        elif player1_x<=0 :
            player1_x = 0
        elif player1_y>=668 :
            player1_y = 668
        elif player1_y<=0 :
            player1_y = 0

        #Modifys player2 position
        player2_x+=player2_xchange
        player2_y+=player2_ychange

        #Modifiying player2 boundaries
        if player2_x>=860 :
            player2_x = 860
        elif player2_x<=0 :
            player2_x = 0
        elif player2_y>=668 :
            player2_y = 668
        elif player2_y<=0 :
            player2_y = 0 

    #Checks the levels and increases the tough ness for every levels 
        if level == 1 or level == 2 :
            calculatescore(boat_y, grass_list, player1_y, player2_y)
            for i in range(0, 4) :
                dispstone(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, i)
                collide = collide_rock(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, player2_x, player2_y)
                if collide :
                    timer_started = False
                    timer_started1 = False
            for i in range(10) :
                boat_x[i]+=boat_xchange[i]
                if boat_x[i] > 820 :
                    boat_x[i] = 820
                    boat_xchange[i]=-x
                if boat_x[i] < 1 :
                    boat_x[i] = 0
                    boat_xchange[i] = x
                dispship(boat_x[i], boat_y[i], i)  
            for i in range(0, 10) :
                collide=collide_boat(boat_x, boat_y, i)
                if collide :
                    timer_started = False
                    timer_started1 = False
            if timer_started :
                passed_time = pygame.time.get_ticks() - start_time
            if timer_started1 :
                pass
            dispplayer1(player1_x, player1_y)
            dispplayer2(player1_x, player1_y)
            if player == 1 :
                passed_time1 = 0
                winner = checkwinner1(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer_started1 = False
                timer(score, score1, passed_time, passed_time1)
                start_time1 = pygame.time.get_ticks()
            if player == 2 :
                passed_time1 = pygame.time.get_ticks() - start_time1
                winner = checkwinner2(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer(score, score1, passed_time, passed_time1)
                player1_y = 720
                player1_x = 450
            if player == 3 :
                level+=1
        elif level == 3 :
            calculatescore(boat_y, grass_list, player1_y, player2_y)
            for i in range(0, 4) :
                dispstone(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, i)
                collide=collide_rock(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, player2_x, player2_y)
                if collide :
                    timer_started = False
                    timer_started1 = False 
            for i in range(10) :
                boat_x[i]+=boat_xchange[i]
                if boat_x[i] > 820 :
                    boat_x[i] = 820
                    boat_xchange[i]=-x
                if boat_x[i] < 1 :
                    boat_x[i] = 0
                    boat_xchange[i] = x 
                dispship(boat_x[i], boat_y[i], i)   
            for i in range(0, 10) :
                collide=collide_boat(boat_x, boat_y, i)
                if collide :
                    timer_started = False
                    timer_started1 = False
            for i in range(8) : 
                danger(skull_x, skull_y, i)
            for i in range(8) :
                collide=collide_skull(skull_x, skull_y)
                if collide :
                    timer_started = False
                    timer_started1 = False
            if timer_started :
                passed_time = pygame.time.get_ticks() - start_time
            if timer_started1 :
                pass
            dispplayer1(player1_x ,player1_y)
            dispplayer2(player1_x ,player1_y)
            if player == 1 :
                passed_time1 = 0
                winner = checkwinner1(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer_started1 = False
                timer(score, score1, passed_time, passed_time1)
                start_time1 = pygame.time.get_ticks()
            if player == 2 :
                passed_time1 = pygame.time.get_ticks() - start_time1
                winner = checkwinner2(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer(score,score1,passed_time,passed_time1)
                player1_y = 720
                player1_x = 450
            if player == 3 :
                level+=1
        elif level == 4 :
            calculatescore(boat_y, grass_list, player1_y, player2_y)
            for i in range(0, 4) :
                dispstone(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, i)
                collide=collide_rock(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, player2_x, player2_y)
                if collide :
                    timer_started = False
                    timer_started1 = False   
            for i in range(10) :
                boat_x[i]+=boat_xchange[i]
                if boat_x[i] > 820 :
                    boat_x[i] = 820
                    boat_xchange[i]=-x
                if boat_x[i] < 1 :
                    boat_x[i] = 0
                    boat_xchange[i] = x
                dispship(boat_x[i], boat_y[i], i) 
            for i in range(0, 10) :
                collide = collide_boat(boat_x, boat_y, i)
                if collide :
                    timer_started = False
                    timer_started1 = False
            for i in range(4) :
                enemy_x[i]+=enemy_xchange
                if enemy_x[i] > 820 :
                    enemy_x[i] = 820
                    enemy_xchange=-12
                if enemy_x[i] < 1 :
                    enemy_x[i] = 0
                    enemy_xchange = 12
                dispenemy(enemy_x, enemy_y, i)
            for i in range(4) :
                collide=collide_enemy(enemy_x[i], enemy_y[i])
            if timer_started :
                passed_time = pygame.time.get_ticks() - start_time
            if timer_started1 :
                pass
            dispplayer1(player1_x, player1_y)
            dispplayer2(player1_x, player1_y)
            if player == 1 :
                passed_time1 = 0
                winner = checkwinner1(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer_started1 = False
                timer(score, score1, passed_time, passed_time1)
                start_time1 = pygame.time.get_ticks()
            if player == 2 :
                passed_time1 = pygame.time.get_ticks() - start_time1
                winner = checkwinner2(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer(score, score1, passed_time, passed_time1)
                player1_y = 720
                player1_x = 450
            if player == 3 :
                level+=1
        elif level == 5 :
            calculatescore(boat_y, grass_list, player1_y, player2_y)
            for i in range(0, 4) :
                dispstone(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, i)
                collide = collide_rock(stone_x, stone_y, rock_x, rock_y, stone1_x, rock1_x, player2_x, player2_y)
                if collide :
                    timer_started = False
                    timer_started1 = False 
            for i in range(10) :
                boat_x[i]+=boat_xchange[i]
                if boat_x[i] > 820 :
                    boat_x[i] = 820
                    boat_xchange[i]=-x
                if boat_x[i] < 1 :
                    boat_x[i] = 0
                    boat_xchange[i] = x
                dispship(boat_x[i], boat_y[i], i)   
            for i in range(0, 10) :
                collide=collide_boat(boat_x, boat_y, i)
                if collide :
                    timer_started = False
                    timer_started1 = False
            for i in range(4) :
                enemy_x[i]+=enemy_xchange
                if enemy_x[i] > 820 :
                    enemy_x[i] = 820
                    enemy_xchange=-12
                if enemy_x[i] < 1 :
                    enemy_x[i] = 0
                    enemy_xchange = 12
                dispenemy(enemy_x, enemy_y, i)
            for i in range(4) :
                collide=collide_enemy(enemy_x[i], enemy_y[i])
            for i in range(8) : 
                danger(skull_x, skull_y, i)
            for i in range(8) :
                collide=collide_skull(skull_x, skull_y)
            if timer_started :
                passed_time = pygame.time.get_ticks() - start_time
            if timer_started1 :
                pass
            dispplayer1(player1_x, player1_y)
            dispplayer2(player1_x, player1_y)
            if player == 1 :
                passed_time1 = 0
                winner = checkwinner1(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer_started1 = False
                timer(score, score1, passed_time, passed_time1)
                start_time1 = pygame.time.get_ticks()
            if player == 2 :
                passed_time1 = pygame.time.get_ticks() - start_time1
                winner = checkwinner2(player1_y, player2_y, score, score1, passed_time, passed_time1)
                timer(score, score1, passed_time, passed_time1)
                player1_y = 720
                player1_x = 450
            if player == 3 :
                level+=1
        elif level == 6 :
            scores(winners)       

#Information on screen will be displayed at the time of start
    else :
        dispstart()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_KP_ENTER :
                timer_started = not timer_started
                if timer_started :
                    start_time = pygame.time.get_ticks()
                timer_started1 = not timer_started1
                if timer_started1 :
                    start_time1 =pygame.time.get_ticks()
                player = 1
                player1_x = 450
                player1_y = 650
                player1_xchange = 0
                player1_ychange = 0
                player2_x = 450
                player2_y = 50
                player2_xchange = 0
                player2_ychange = 0
                index = 0
                score = 0
                index1 = 0
                score1 = 0
                index3 = 4
                index4 = 4
                passed_time = 0
                passed_time1 = 0
                x+=5
                boat_xchange = []
                for i in range(0,10):
                    boat_xchange.append(x)
                gamestart=True
    
#checks the winners and displays them on the score,time on the screen after game complete's
        if level == 2 or level == 3 or level == 4 or level == 5 or level == 6 :
            if score == score1 : 
                if  passed_time > passed_time1 :
                    gameover('Player 2', score1, passed_time1, 'Player 1', score, passed_time, level-1)
                elif passed_time < passed_time1 :
                    gameover('Player 1', score, passed_time, 'Player 2', score1, passed_time1, level-1)
                elif passed_time == passed_time1 :
                    root.blit(win, (0, 0))
                    text = font1.render("Match has Tied", True, font_color1)  
                    root.blit(text, (300, 340))
            elif lost == 'player1':
                if score == score1 :
                    if  passed_time > passed_time1 :
                        gameover('Player 2', score1, passed_time1, 'Player 1', score, passed_time, level-1)
                    elif passed_time<passed_time1:
                        gameover('Player 1', score, passed_time, 'Player 2', score1, passed_time1, level-1)
                    elif passed_time == passed_time1:
                        root.blit(win, (0, 0))
                        text = font1.render("Match has Tied", True, font_color1)  
                        root.blit(text, (300, 340))
                elif score < score1 :
                    gameover('Player 2', score1, passed_time1,'Player 1', score, passed_time, level-1)
                elif score>score1:
                    gameover('Player 1', score, passed_time, 'Player 2', score1, passed_time1, level-1)                                   
                elif score1 == 70 :
                    gameover('Player 2', score1, passed_time1, 'Player 1', score, passed_time, level-1)               
            elif lost == 'player2' :
                if score == score1 :
                    if  passed_time > passed_time1 :
                        gameover('Player 2', score1, passed_time1, 'Player 1', score, passed_time, level-1)
                    elif passed_time < passed_time1 :
                        gameover('Player 1', score, passed_time, 'Player 2', score1, passed_time1, level-1)
                    elif passed_time == passed_time1 :
                        root.blit(win, (0, 0))
                        text = font1.render("Match has Tied", True, font_color1)  
                        root.blit(text ,(300, 340))
                if score > score1 :
                    gameover('Player 1', score, passed_time, 'Player 2', score1, passed_time1, level-1)
                if score<score1:
                    gameover('Player 2', score1, passed_time1, 'Player 1', score, passed_time, level-1)              
                if score == 70 :
                    gameover('Player 1', score, passed_time, 'Player 2', score1, passed_time1, level-1)
    pygame.display.update()
pygame.quit()