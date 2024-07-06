#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:17:13 2024

@author: alyssaking
"""

import pygame
from sys import exit
from random import choice

class MovingArrows(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.arrow_type = type
		
        if type == 'up':
            self.image = pygame.image.load('Rhythm - arrow images/up_arrow_move.png').convert_alpha()
            x_pos = 400
            
        elif type == 'left':
            self.image = pygame.image.load('Rhythm - arrow images/left_arrow_move.png').convert_alpha()
            x_pos = 175
            
        elif type =='right':
            self.image = pygame.image.load('Rhythm - arrow images/right_arrow_move.png').convert_alpha()
            x_pos = 600
        
        self.image = pygame.transform.scale(self.image, (100,100))    
        self.rect = self.image.get_rect(midbottom = (x_pos, -50))
        
    def update(self):
        self.rect.y += 6
        self.destroy()
        
    def destroy(self):
        if self.rect.y >= 800:
            self.kill()
	

pygame.init()

screen = pygame.display.set_mode((800,700))
pygame.display.set_caption('Rhythm Master')
clock = pygame.time.Clock()

test_font = pygame.font.Font('Rhythm - fonts/Pixeltypecopy.ttf', 50)
test_font2 = pygame.font.Font('Rhythm - fonts/8-bit-hud.ttf', 40)
test_font3 = pygame.font.Font('Rhythm - fonts/8-bit-hud.ttf', 20)

game_active = False

game_sound = pygame.mixer.Sound('Rhythm - music/Be_Your_Girl_Kaytranada.mp3')

arrow_counter = 0 
score = 0
combo = 0
max_combo = 0

pink_cloud = pygame.image.load('Rhythm - icons and backgrounds/cloud_pink_bg.jpeg').convert()
pink_cloud_rect = pink_cloud.get_rect(center =(400,345))

start_button = pygame.image.load('Rhythm - icons and backgrounds/start_button.png').convert_alpha()
start_button = pygame.transform.scale(start_button, (350,100))
start_button_rect = start_button.get_rect(center = (400,500))

music_icon = pygame.image.load('Rhythm - icons and backgrounds/music_icon.png').convert_alpha()
music_icon = pygame.transform.scale(music_icon, (200,250))
music_icon_rect = music_icon.get_rect(center = (400, 300))

game_name = test_font2.render('Rhythm Master',False,'#ff028d')
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press start to begin',False, '#ff028d')
game_message_rect = game_message.get_rect(center = (400,600))

city_bg = pygame.image.load('Rhythm - icons and backgrounds/pastel_city_bg.png').convert()
city_bg = pygame.transform.scale(city_bg, (1350,800))
city_bg_rect = city_bg.get_rect(center =(400,370))

left_arrow_still = pygame.image.load('Rhythm - arrow images/left_arrow_still.png').convert_alpha()
left_arrow_still = pygame.transform.scale(left_arrow_still, (100,100))
left_arrow_still_rect = left_arrow_still.get_rect(midbottom = (175, 650))

right_arrow_still = pygame.image.load('Rhythm - arrow images/right_arrow_still.png').convert_alpha()
right_arrow_still = pygame.transform.scale(right_arrow_still, (100,100))
right_arrow_still_rect = right_arrow_still.get_rect(midbottom = (600, 650))

up_arrow_still = pygame.image.load('Rhythm - arrow images/up_arrow_still.png').convert_alpha()
up_arrow_still = pygame.transform.scale(up_arrow_still, (100,100))
up_arrow_still_rect = up_arrow_still.get_rect(midbottom = (400,650))


moving_arrows_group = pygame.sprite.Group()
moving_arrows_timer = pygame.USEREVENT + 1
pygame.time.set_timer(moving_arrows_timer,500)


def display_score(score):
    score_message = test_font3.render(f'Score: {score}',False,('Purple'))
    score_message_rect = score_message.get_rect(midleft = (10,70))
    screen.blit(score_message, score_message_rect)


def display_combo(combo):
    combo_message = test_font3.render(f'Combo: {combo}',False,('Purple'))
    combo_message_rect = combo_message.get_rect(midleft = (10,100))
    screen.blit(combo_message, combo_message_rect)
    
    
def display_okay(arrow_type):
    
    okay_message = test_font.render(str('Okay!'),False,('White'))
   
    if arrow_type == 'up':
        okay_message_rect = okay_message.get_rect(center = (500,665))
     
       
    elif arrow_type == 'left':
        okay_message_rect = okay_message.get_rect(center = (290,665))
        
    elif arrow_type == 'right':
        okay_message_rect = okay_message.get_rect(center = (650,665))
    screen.blit(okay_message,okay_message_rect)
    

def display_great(arrow_type):
   
    great_message = test_font.render(str('Great!'),False,('White'))
   
    if arrow_type == 'up':
        great_message_rect = great_message.get_rect(center = (500,665))
       
    elif arrow_type == 'left':
        great_message_rect = great_message.get_rect(center = (290,665))
        
    elif arrow_type == 'right':
        great_message_rect = great_message.get_rect(center = (650,665))
    screen.blit(great_message,great_message_rect)
    
 
def update_game_state_okay(score, combo, max_combo, arrow):
    score += 5
    display_score(score)
    
    combo += 1
    display_combo(combo)
    
    display_okay(arrow.arrow_type)
    max_combo = max(max_combo, combo)
    arrow.kill()
    
    return score, combo, max_combo

def update_game_state_great(score, combo, max_combo, arrow):
    score += 10
    display_score(score)
    
    combo += 1
    display_combo(combo)
    
    display_great(arrow.arrow_type)
    max_combo = max(max_combo, combo)
    arrow.kill()
    
    return score, combo, max_combo



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == moving_arrows_timer:
                arrow_counter+=1
                moving_arrows_group.add(MovingArrows(choice(['up','left','right'])))
                

    if game_active:
            
                       
        
        # game active background     
        screen.blit(city_bg, city_bg_rect)
        pygame.draw.line(screen,'White', (250,50), (250,600),  5) # line 1
        pygame.draw.line(screen,'White', (525,50), (525,600),  5) # line 2
       
        display_score(score)
        display_combo(combo)
        
        #displays still arrows
        screen.blit(left_arrow_still, left_arrow_still_rect)
        screen.blit(right_arrow_still, right_arrow_still_rect)
        screen.blit(up_arrow_still, up_arrow_still_rect)
        
        #generates moving arrows    
        moving_arrows_group.draw(screen)
        moving_arrows_group.update()
        
        keys = pygame.key.get_pressed()
        
        
      
            
        for arrow in moving_arrows_group:
            
            
            
            if arrow_counter > 528:
                # 528 is the number of arrows to complete the song 
                for arrow in moving_arrows_group:
                    if arrow.rect.bottom < 0:
                        arrow.kill()
                # kills new arrows once song is over 
                if len(moving_arrows_group) == 0: 
                   # once remaining arrows meet the bottom and there are no more arrows being generated/on screen set game active to False
                    game_active = False
            
            
            if arrow.arrow_type == 'up' and up_arrow_still_rect.colliderect(arrow.rect):
                if keys[pygame.K_UP]:
                    if 550 < arrow.rect.bottom < 600 or arrow.rect.bottom > 650:
                        score, combo, max_combo = update_game_state_okay(score, combo, max_combo, arrow)
                       
                        
                    elif 600 <= arrow.rect.bottom <= 650 :
                        score, combo, max_combo = update_game_state_great(score, combo, max_combo, arrow)
                         
                else: 
                    if arrow.rect.bottom > 725:
                        combo = 0
                        display_combo(combo)
                        
                        
                    
                    
                        
            elif arrow.arrow_type == 'left' and left_arrow_still_rect.colliderect(arrow.rect):
                if keys[pygame.K_LEFT]:
                    if 550 < arrow.rect.bottom < 600 or arrow.rect.bottom > 650:
                        score, combo, max_combo = update_game_state_okay(score, combo, max_combo, arrow)
                    
                    elif 600 <= arrow.rect.bottom <= 650 :
                        score, combo, max_combo = update_game_state_great(score, combo, max_combo, arrow)

                   
                else: 
                    if arrow.rect.bottom > 725:
                        combo = 0
                        display_combo(combo)
                    
            
       
           
            elif arrow.arrow_type == 'right' and right_arrow_still_rect.colliderect(arrow.rect):
                if keys[pygame.K_RIGHT]:
                    if 550 < arrow.rect.bottom < 600 or arrow.rect.bottom > 650:
                        score, combo, max_combo = update_game_state_okay(score, combo, max_combo, arrow)
                        
            
                        arrow.kill()
                    elif 600 <= arrow.rect.bottom <= 650 :
                        score, combo, max_combo = update_game_state_great(score, combo, max_combo, arrow)

                else: 
                    if arrow.rect.bottom > 725:
                        combo = 0
                        display_combo(combo)
                        
                        
        
    
            
                  
       
    if not game_active:
           
           screen.blit(pink_cloud, pink_cloud_rect)
           screen.blit(game_name, game_name_rect) #"Rhythm Master"
           screen.blit(start_button, start_button_rect) #Start Button" 
           screen.blit(game_message, game_message_rect)  #Click here to start"           
           screen.blit(music_icon, music_icon_rect) # music icon
            
           if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(pygame.mouse.get_pos()):
               
              game_sound.play(loops = 0)  # start song
              game_active = True
                # press start to begin
                # if start is press set game to active 
             
           if score != 0:
               score_message = test_font3.render(str('Your Score: ') + str(score) +'    Max Combo: ' + str(max_combo),False,('Purple'))
               score_message_rect = score_message.get_rect(center = (400,130))
               screen.blit(score_message,score_message_rect)
               
                # press start to begin
                # if start is press set game to active 
           if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(pygame.mouse.get_pos()):
               # reset to 0
               arrow_counter = 0
               score = 0
               combo = 0
               max_combo = 0
               
               
               for arrow in moving_arrows_group:
                   arrow.kill()
            # gets rid of the rest of the arrows 
               game_active = True
                    #play_sound
    pygame.display.update()
    clock.tick(60)