import pygame
import math
import pygame_widgets
from pygame_widgets.button import Button
from time import sleep


def get_distance(start_pos, center_pos):
    return ''
    return math.sqrt(math.pow(start_pos[0] - center_pos[0], 2) + math.pow(start_pos[1] - center_pos[1], 2))


def get_azimuth(start_pos, center_pos, dx):
    if start_pos[0] == center_pos[0]:
        return 90
        #return math.pi / 2
    dy = math.tan(70 / 57.3) * dx
    if center_pos[0] < start_pos[0]:
        rad = math.pi - math.atan(dy / abs(start_pos[0] - center_pos[0]))
    else:
        rad = math.atan(dy / abs(start_pos[0] - center_pos[0]))

    # if center_pos[0] < start_pos[0]:
    #     rad = math.pi - math.atan(abs(start_pos[1] - center_pos[1]) / abs(start_pos[0] - center_pos[0]))
    # else:
    #     rad = math.atan(abs(start_pos[1] - center_pos[1]) / abs(start_pos[0] - center_pos[0]))
    return rad * 57.3


def change_line(parameters):
    parameters['show_line'] *= -1
    print('click')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (16, 117, 0)
GREY = (128,128,128)

pygame.init()

width = 1024
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Prototype")
parameters = {'show_line': 1}

button = Button(screen, width - 200, height - 100, 150, 50,
    text='Show/delete line', fontSize=20, margin=20, radius=10)

circle_pos = [width / 2, height / 4]
circle_radius = 30
circle_speed = 5
radius_growth = 1
rect_height = 200
font = pygame.font.SysFont("Consolas", 20)
pygame.display.flip()

while True:
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, height - rect_height, width, rect_height))
    text1 = font.render(f"X: {-width / 2 + circle_pos[0]}   Y: {circle_pos[1]}", True, BLACK)
    screen.blit(text1, (20, height - rect_height + 20))
    text2 = font.render(f"Distance: {get_distance((width / 2, height - rect_height), circle_pos)}", True, BLACK)
    screen.blit(text2, (20, height - rect_height + 70))
    text3 = font.render(f"Azimuth: {get_azimuth((width / 2, height - rect_height), circle_pos, width/2)}", True, BLACK)
    screen.blit(text3, (20, height - rect_height + 120))
    text4 = font.render(f"G_obj: {circle_radius}", True, BLACK)
    screen.blit(text4, (20, height - rect_height + 170))

    # pygame.draw.circle(screen, GREY, (width / 2, height - rect_height), 5)
    if parameters['show_line'] == 1:
        pygame.draw.line(screen, GREY, (0, height / 4), (width, height / 4), 1)
    # pygame.draw.line(screen, GREY, (width / 2, height - rect_height), circle_pos, 1)
    pygame.draw.circle(screen, GREEN, circle_pos, circle_radius)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if circle_pos[0] - circle_radius - circle_speed >= 0:
            circle_pos[0] -= circle_speed
    if keys[pygame.K_RIGHT]:
        if circle_pos[0] + circle_radius + circle_speed <= width:
            circle_pos[0] += circle_speed
    if keys[pygame.K_UP]:
        if circle_pos[1] + circle_radius + radius_growth <= height - rect_height:
            circle_radius += radius_growth
    if keys[pygame.K_DOWN]:
        if circle_radius - radius_growth > 0:
            circle_radius -= radius_growth
    if button.clicked:
        change_line(parameters)

    pygame_widgets.update(events)
    pygame.display.update()
    pygame.time.Clock().tick(60)
