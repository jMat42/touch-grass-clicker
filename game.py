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