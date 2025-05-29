import time

import pygame
from pygame import K_LEFT, K_RIGHT

pygame.init()
clock = pygame.time.Clock()


#load sound
bounce_sound = pygame.mixer.Sound("./sounds/bounce.wav")
hit_sound = pygame.mixer.Sound("./sounds/hit.wav")

#screen setting
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("brick breaker")


#color
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#paddle setting
paddle = pygame.Rect(0,0, 100, 15)
paddle.center = (width/2, height-30)
paddle_speed = 5


#ball setting
radius = 10
ball = pygame.Rect(0, 0, radius * 2, radius * 2)
ball.center = (width/2, height/2)
ball_dx = 5
ball_dy = -5

#brick setting
bricks = []
rows = 5
cols = 10
brick_width = 75
brick_height = 20
num_brick = rows * cols

game_won = False


for row in range(rows):
    for col in range(cols):
        brick = pygame.Rect(20 + col * brick_width,  50 + row * brick_height, brick_width-5, brick_height-5)
        bricks.append(brick)



def draw_brick():
    for brick in bricks:
        pygame.draw.rect(screen, green, brick)



def move_ball():
    global  ball_dx, ball_dy, lives, game_over, num_brick
    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0:
        ball_dy *= -1

    if ball.bottom >= height:
        lives -= 1
        reset_ball()
        if lives <= 0 :
            game_over = True

    if ball.left <=0 or ball.right >= width:
        ball_dx *= -1

    if ball.colliderect(paddle):
        bounce_sound.play()
        ball_dy *= -1

    for brick in bricks:
        if brick.colliderect(ball):
            ball_dy *= -1
            hit_sound.play()
            bricks.remove(brick)
            num_brick -= 1
            if num_brick <= 0:
                game_over = True
                game_won = True

            break

def reset_ball():
    ball.center = (width/2, height/2)

game_over = False
lives = 3


#text
font = pygame.font.Font(None, 30)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle.x >= 0:
        paddle.x -= paddle_speed
    if keys[K_RIGHT] and paddle.right <= width:
        paddle.x += paddle_speed


    screen.fill(white)
    pygame.draw.rect(screen, black, paddle)
    pygame.draw.ellipse(screen, blue, ball)
    if game_over:
        text = font.render("Game over!" if not game_won else "YOU Won", True, red if not game_won else blue)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, height / 2)
        screen.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
        running = False


    draw_brick()


    move_ball()
    pygame.display.update()
    clock.tick(60)




pygame.quit()