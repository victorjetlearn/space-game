import pygame
import os
import time

pygame.init()
width = 1000
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("space invader game")
velocity = 0.75
fps = 60
bullet_velocity = 3
RED_HIT = pygame.USEREVENT+1
YELLOW_HIT = pygame.USEREVENT+2
font = pygame.font.SysFont("Ariel", 40)
yellow_win = font.render("Yellow wins!",1,"yellow")
red_win = font.render("Red wins!",1,"red")



background = pygame.transform.scale(pygame.image.load (os.path.join("background.png")),(width,height))
ship1 = pygame.image.load(os.path.join("ship1.png"))
ship1red = pygame.transform.rotate(pygame.transform.scale(ship1,(60,40)),90)
ship2 = pygame.image.load(os.path.join("ship2.png"))
ship2yellow = pygame.transform.rotate(pygame.transform.scale(ship2,(60,40)),270)

def drawwindow(red,yellow,red_bullets,yellow_bullets):
    screen.blit(background,(0,0))
    screen.blit(ship1red,(red.x,red.y))
    screen.blit(ship2yellow,(yellow.x,yellow.y))
    for i in red_bullets:
        pygame.draw.rect(screen, "red",i)
    for i in yellow_bullets:
        pygame.draw.rect(screen, "yellow",i)

    
    pygame.display.update()

def yellow_ship_mov(key_press, yellow):
    if key_press[pygame.K_LEFT]:
        yellow.x -= velocity
    if key_press[pygame.K_RIGHT]:
        yellow.x += velocity
    if key_press[pygame.K_UP]:
        yellow.y -= velocity
    if key_press[pygame.K_DOWN]:
        yellow.y += velocity

def red_ship_mov(key_press, red):
    if key_press[pygame.K_a]:
        red.x -= velocity
    if key_press[pygame.K_d]:
        red.x += velocity
    if key_press[pygame.K_w]:
        red.y -= velocity
    if key_press[pygame.K_s]:
        red.y += velocity

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    global yellow_win, red_win
    for i in yellow_bullets:
        i.x -= bullet_velocity
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(RED_HIT))
            screen.blit(yellow_win,(400,300))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            
        
    for i in red_bullets:
        i.x += bullet_velocity
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            screen.blit(red_win,(400,300))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
    
    
            

def main():
    red = pygame.Rect(100,300,60,40)
    yellow = pygame.Rect(700,300,60,40)

    red_bullets = []
    yellow_bullets = []

    while True:
            
        for i in pygame.event.get():
                
            if i.type == pygame.QUIT:
                    pygame.quit()



            if i.type == pygame.KEYDOWN:
                if i.key== pygame.K_LSHIFT:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height// 2 -2, 10,5)
                    red_bullets.append(bullet)
                if i.key== pygame.K_RSHIFT:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height// 2 -2, 10,5)
                    yellow_bullets.append(bullet)
        key_press = pygame.key.get_pressed()
        red_ship_mov(key_press, red)
        yellow_ship_mov(key_press, yellow)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        drawwindow(red,yellow,red_bullets,yellow_bullets)
  
if __name__ == "__main__":
    main()

            


