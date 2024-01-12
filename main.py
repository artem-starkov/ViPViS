import pygame
import math
import pygame_widgets
from pygame_widgets.button import Button
from time import sleep

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (16, 117, 0)
GREY = (128, 128, 128)
pygame.init()


class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coords(self):
        return tuple([self.x, self.y])


class MovingPrototype:
    def __init__(self, width=1024, height=720, circle_speed=3, radius = 30):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.show_line = 1
        self.info_block_height = 0
        self.circle = Figure(width / 2, (height - self.info_block_height) / 2)
        self.radius = radius * 2
        self.eye = Figure(width / 2, height - self.info_block_height)
        self.radius_growth = 1
        self.circle_speed = circle_speed
        self.direction = 1
        self.font = pygame.font.SysFont("Consolas", 20)
        # self.init_objects()

    def init_objects(self):
        button = Button(self.screen, self.width - 200, self.height - 100, 150, 50,
                        text='Show/delete line', fontSize=20, margin=20, radius=10, onClick=self.change_line)

    def get_distance(self):
        return ''
        return math.sqrt(math.pow(self.eye.x - self.circle.x, 2) + math.pow(self.eye.y - self.circle.y, 2))

    def get_azimuth(self):
        dx = self.width/2
        if self.eye.x == self.circle.x:
            return 90
        dy = math.tan(70 / 57.3) * dx
        if self.circle.x < self.eye.x:
            rad = math.pi - math.atan(dy / abs(self.eye.x - self.circle.x))
        else:
            rad = math.atan(dy / abs(self.eye.x - self.circle.x))
        return rad * 57.3

    def draw_objects(self):
        self.screen.fill(GREY)
        pygame.draw.rect(self.screen, WHITE, (0, self.height - self.info_block_height,
                                              self.width, self.info_block_height))
        if self.show_line == 1:
            pygame.draw.line(self.screen, GREY, (0, self.height / 4),
                             (self.width, self.height / 4), 1)
        #pygame.draw.circle(self.screen, GREEN, self.circle.coords(), self.radius)

        image = pygame.image.load("round2.png").convert_alpha()
        image.set_colorkey((255, 255, 255))
        image = pygame.transform.scale(image, (self.radius * 2, self.radius * 2))
        self.screen.blit(image, image.get_rect(center=self.circle.coords()))

    def display_text(self):
        text1 = self.font.render(f"X: {-self.width / 2 + self.circle.x}   Y: {self.circle.y}", True, BLACK)
        self.screen.blit(text1, (20, self.height - self.info_block_height + 20))
        text2 = self.font.render(f"Distance: {self.get_distance()}", True, BLACK)
        self.screen.blit(text2, (20, self.height - self.info_block_height + 70))
        text3 = self.font.render(f"Azimuth: {self.get_azimuth()}", True, BLACK)
        self.screen.blit(text3, (20, self.height - self.info_block_height + 120))
        text4 = self.font.render(f"G_obj: {self.radius / 2}", True, BLACK)
        self.screen.blit(text4, (20, self.height - self.info_block_height + 170))

    def process_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.circle.x - self.radius - self.circle_speed >= 0:
                self.circle.x -= self.circle_speed
        if keys[pygame.K_RIGHT]:
            if self.circle.x + self.radius + self.circle_speed <= self.width:
                self.circle.x += self.circle_speed
        if keys[pygame.K_UP]:
            if self.circle.y + self.radius + self.radius_growth <= self.height - self.info_block_height:
                self.radius += self.radius_growth
        if keys[pygame.K_DOWN]:
            if self.radius - self.radius_growth > 0:
                self.radius -= self.radius_growth

    def process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame_widgets.update(events)

    def change_line(self, ):
        self.show_line *= -1

    def start(self):
        pygame.display.set_caption("Prototype")
        pygame.display.flip()
        while True:
            self.draw_objects()
            self.display_text()
            # self.process_keyboard()
            self.process_events()
            if self.direction > 0:
                if self.circle.x - self.radius - self.circle_speed >= 0:
                    self.circle.x -= self.circle_speed
                else:
                    self.direction *= -1
            else:
                if self.circle.x + self.radius + self.circle_speed <= self.width:
                    self.circle.x += self.circle_speed
                else:
                    self.direction *= -1

            pygame.display.update()
            pygame.time.Clock().tick(60)


prototype = MovingPrototype(circle_speed=5, radius=50)
prototype.start()
