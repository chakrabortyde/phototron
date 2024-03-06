import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
ROBOT_SIZE = 50
ROBOT_CATCH_RADIUS = 25
OBSTACLE_WIDTH = 100
OBSTACLE_HEIGHT = 50
INCLINE_HEIGHT = 200
INCLINE_ANGLE = 30
BALL_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Catcher")


# Define classes
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed


class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ROBOT_SIZE, ROBOT_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (
        SCREEN_WIDTH // 2, SCREEN_HEIGHT - INCLINE_HEIGHT - ROBOT_SIZE // 2)

    def update(self):
        # Implement robot movement here
        pass


# Create sprites groups
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
robots = pygame.sprite.Group()

# Create the robot
robot = Robot()
robots.add(robot)
all_sprites.add(robot)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Spawn new balls
    if random.randint(1, 100) < 5:
        color = random.choice(BALL_COLORS)
        x = random.randint(0, SCREEN_WIDTH)
        y = 0
        ball = Ball(color, x, y)
        balls.add(ball)
        all_sprites.add(ball)

    # Collision detection
    for ball in balls:
        if pygame.sprite.spritecollide(ball, robots, False):
            # Ball caught
            balls.remove(ball)
            all_sprites.remove(ball)
            # Implement scoring logic here

    # Draw
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - INCLINE_HEIGHT, SCREEN_WIDTH, INCLINE_HEIGHT))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
