import pygame
from brain import movement_bat, movement_moth, detect, detect_bat
from position import distance
def move(mothLife, batLife, screen, WIDTH, HEIGHT):
    for moths in mothLife:
        if moths[2] <= 0:
            mothLife.remove(moths)
            print(f"Moth Starvated. {len(mothLife)} left")
        for bats in batLife:
            if distance(moths[0], bats[0]) < 20:
                bats[2] += moths[2]
                mothLife.remove(moths)
                # print(f"Killed. {len(mothLife)} left, becomes {bats[2]} Energy")
                break

        movement_moth(moths)
        if moths[0].left <= 0: moths[0].left = 0
        if moths[0].right >= WIDTH: moths[0].right = WIDTH
        if moths[0].top <= 0: moths[0].top = 0
        if moths[0].bottom >= HEIGHT: moths[0].bottom = HEIGHT
        
        
    for bats in batLife:
        if bats[2] <= 0:
            ran = bats[1][3]/2
            batLife.remove(bats)
            print(f"Bat Starvated. {len(batLife)} left. Range was {ran}")
        
        movement_bat(bats)
        if bats[0].left <= 0 + 0: bats[0].left = 0 + 0
        if bats[0].right >= WIDTH - 0: bats[0].right = WIDTH - 0
        if bats[0].top <= 0 + 0: bats[0].top = 0 + 0
        if bats[0].bottom >= HEIGHT - 0: bats[0].bottom = HEIGHT - 0
        
    

def draw(mothLife, batLife, screen, WIDTH, HEIGHT, WHITE):
    
    screen.fill(WHITE)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 50, WIDTH - 100, HEIGHT - 100))


    for bats in batLife:
        detect_bat(bats, mothLife)
        pygame.draw.circle(screen, (0, 255, 0), bats[1].center, bats[1][3]/2)

    for moths in mothLife:
        pygame.draw.circle(screen, (255, 0, 255), moths[1].center, moths[1][3]/2)

        
    for bats in batLife:
        pygame.draw.circle(screen, (255, 0, 0), bats[0].center, 20)
        

    for moths in mothLife:
        detect(moths, batLife, screen)
        

    pygame.display.flip()
