
import pygame
import random

pygame.init()

width = 800
height = 600

clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong game")

player = pygame.Rect(0, 0, 20, 100)
player.centery = height/2
player.x = 10

cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery = height/2
cpu.x = width-30

ball = pygame.Rect(0, 0, 30, 30)
ball.center = (width/2, height/2)

ball_speed_x = 5
ball_speed_y = 5

player_speed = 5
cpu_speed = 5

player_score = 0
cpu_score = 0




def move_ball():
    global ball_speed_x, ball_speed_y, cpu_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.left <=0:
        cpu_score += 1
        reset_ball()

    if ball.right >= width:
        player_score +=1
        reset_ball()

    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1


def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top >= 0:
        player.y -= player_speed

    if keys[pygame.K_DOWN] and player.bottom <= height:
        player.y += player_speed

def move_cpu():
    if ball.centery > cpu.centery and cpu.bottom <= height:
        cpu.y += cpu_speed
    if ball.centery < cpu.centery and cpu.top >= 0:
        cpu.y -= cpu_speed

def reset_ball():
    global  ball_speed_x, ball_speed_y
    ball.center = (width/2, height/2)
    ball_speed_x *= random.choice([1, -1 ])
    ball_speed_y *= random.choice([1, -1])


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






    screen.fill('black')
    pygame.draw.aaline(screen, 'white', (width/2, 0), (width/2, height))
    pygame.draw.rect(screen,'white', player)
    pygame.draw.rect(screen, 'white', cpu)
    pygame.draw.ellipse(screen, 'white', ball)

    player_speed_surface = font.render(str(player_score), 1, 'white' )
    cpu_speed_surface =  font.render(str(cpu_score), 1, 'white')

    screen.blit(player_speed_surface, (1/4*width, 10))
    screen.blit(cpu_speed_surface, (3 / 4 * width, 10))


    move_ball()
    move_player()
    move_cpu()

    clock.tick(60)
    pygame.display.update()

pygame.quit()