import pygame
import os
from pygame import mixer
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bat - Luna Edition")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

WHITE = (255,255,255)
FPS = 60
VEL = 4
speed = 3

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 60)

BK_HIT = pygame.USEREVENT + 1

#RBI = red bat image
#BBI = black bat image
R_B_I = pygame.image.load('red.png')
B_B_I = pygame.image.load('black.png')

#background
background = pygame.image.load('background.png')

#background sound
mixer.init()
music = mixer.music.load('backsound.ogg')
mixer.music.play(-1)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_window(rd, bk, bk_health):
    WIN.fill(WHITE)
    WIN.blit(background, (0,0))
    bk_health_text = HEALTH_FONT.render(
        "Health: " + str(bk_health), 1, WHITE)
    WIN.blit(bk_health_text,(3,3))
    WIN.blit(R_B_I, (rd.x,rd.y))
    WIN.blit(B_B_I,(bk.x, bk.y))
    pygame.display.update()
    
def main():
    bk = pygame.Rect(10, 10, 49, 27.5)
    rd = pygame.Rect(10, 400, 49, 27.5)    
    
    bk_health = 100
    rd_health = 100
    
    clock= pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == BK_HIT:
                bk_health -= 1
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #LEFT
            bk.x -= VEL
        if keys_pressed[pygame.K_d]: #right
            bk.x += VEL
        if keys_pressed[pygame.K_s]: #down
            bk.y += VEL
        if keys_pressed[pygame.K_w]: #up
            bk.y -= VEL
            
        if rd.x > bk.x: # If the red bat is to the right of the black bat
            rd.x -= speed #Move the bat to the left
        elif rd.x < bk.x: # If the red bat is to the left of the black bat
            rd.x += speed #Move the bat to the right
        if rd.y > bk.y: # If the red bat is to the right of the black bat
            rd.y -= speed #Move the bat to the left
        elif rd.y < bk.y: # If the red bat is to the left of the black bat
            rd.y += speed #Move the bat to the right
            
        if rd.colliderect(bk):
            pygame.event.post(pygame.event.Event(BK_HIT))
            
                 
  
        winner_text = ""
        if bk_health <= 0:
            winner_text = "Red Bat Wins!"

        if rd_health <= 0:
            winner_text = "Black Bat Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break
 
        draw_window(rd, bk, bk_health)
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
