import pygame
import time
import random
pygame.font.init()

#WINDOW SIZE
WIDTH, HEIGTH = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Python Game")

#BACKGORUND THAT IS USED IN THE WINDOW
BACKGROUND = pygame.transform.scale(pygame.image.load("background.jpeg"), (WIDTH, HEIGTH)) #SCALING THE BACKGROUND DEPENDING ON THE WINDOW SIZE AND BACKGROUND IMAGE SIZE

#PLAYER SIZE AND MOVEMENT
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 5

#LASER SIZE AND MOVEMENT
LASER_WIDTH = 10
LASER_HEIGHT = 20
LASER_VELOCITY = 3

FONT = pygame.font.SysFont("Arial", 25)#FONT TYPE AND SIZE

def draw(player, elapsed_time, lasers): 
    WINDOW.blit(BACKGROUND, (0, 0)) #BACKGROUND IS STARTING FROM POSITION 0,0

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10)) #RENDERING TIME

    pygame.draw.rect(WINDOW, "purple", player) #CHARACTER WHICH WILL BE USED

    for laser in lasers:
        pygame.draw.rect(WINDOW, "red", laser)

    pygame.display.update()



def main():

    run = True

    player = pygame.Rect(200, HEIGTH - PLAYER_HEIGHT, 
    PLAYER_WIDTH, PLAYER_HEIGHT) # STARTING POSISTION OF THE PLAYER

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    laser_add_increment = 2000
    laser_count = 0

    lasers = []
    hit = False

    while run: #WINDOW OPERATRION
        laser_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if laser_count > laser_add_increment: #GENERATING ALL THE LASERS
            for _ in range(3):
                laser_x = random.randint(0, WIDTH - LASER_WIDTH) 
                laser = pygame.Rect(laser_x, - LASER_HEIGHT, LASER_WIDTH, LASER_HEIGHT)
                lasers.append(laser)
            
            laser_add_increment = max(200, laser_add_increment - 50)
            laser_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0: #LEFT ARROW KEY MOVEMENT FOR PLAYER
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH: #RIGHT ARROW KEY MOVEMENT FOR PLAYER
            player.x += PLAYER_VELOCITY

        for laser in lasers[:]: #MOVEMENT OF THE LASERS
            laser.y += LASER_VELOCITY
            if laser.y > HEIGTH:
                lasers.remove(laser)
            elif laser.y + laser.height >= player.y and laser.colliderect(player):
                lasers.remove(laser)
                hit = True
                break

        if hit:
            lost_text = FONT.render("YOU LOST!", 1, "RED")
            WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGTH/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break




        draw(player, elapsed_time, lasers)

    pygame.quit()

if __name__ == "__main__":
    main()
