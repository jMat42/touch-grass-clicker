import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Touch Grass Clicker")
clock = pygame.time.Clock()

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
BLUE = (0, 122, 255)
HOVER_BLUE = (0, 150, 255)

# Variables:
grass_touched = 0
font = pygame.font.SysFont("Ohno Soft", 40)

# make button
button_rect = pygame.Rect(200, 200, 200, 100)

# main game loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_pos):
                grass_touched += 1

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the button
    button_color = HOVER_BLUE if button_rect.collidepoint(mouse_pos) else BLUE
    pygame.draw.rect(screen, button_color, button_rect)

    # Draw the text
    text = font.render(f"Grass Touched: {grass_touched}", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 100))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()