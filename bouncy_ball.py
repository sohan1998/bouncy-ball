
import sys, os
import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
OBSTACLE_GAP = 175
BALL_RADIUS = 20

pygame.init()

SCREEN_DIMENSIONS = screenX, screenY = (700, 500)
FPS = 60


screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Bouncy Ball")

clock = pygame.time.Clock()


def ball(x,y):
	pygame.draw.circle(screen, BLACK, [x,y], BALL_RADIUS)

def gameOver():
	font = pygame.font.SysFont(None, 50)
	text = font.render("GAME OVER", True, RED)
	screen.blit(text, [300, 100])
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				pygame.quit()
				sys.exit()

def obstacle(xloc, yloc, xsize, ysize):
	pygame.draw.rect(screen, GREEN, [xloc, yloc, xsize,ysize])
	pygame.draw.rect(screen, GREEN, [xloc, int(yloc + ysize + OBSTACLE_GAP), xsize, ysize + screenY])

def Score(score):
	font = pygame.font.SysFont(None, 35)
	text = font.render("Score :  " + str(score), True, BLACK)
	screen.blit(text, [10, 10])

x = screenX//2
y = screenY//2
x_speed = 0
y_speed = 0
ground = screenY - 25
xloc = 700
yloc = 0
xsize = 70
ysize = randint(50, 300)
obstacle_speed = 2
score = 0


while True:
	keyPressed = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT or keyPressed[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				y_speed = -8
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				y_speed = 4

	screen.fill(WHITE)
	obstacle(xloc, yloc, xsize, ysize)
	ball(x,y)
	Score(score)

#	x += x_speed
	y += y_speed
	xloc -= obstacle_speed

	if y > ground:
#		gameOver()
		y_speed = 0
		obstacle_speed = 0
		gameOver()

	if x+BALL_RADIUS > xloc and y-BALL_RADIUS < ysize and x-15 < xsize+xloc:
		# gameOver()
		y_speed = 0
		obstacle_speed = 0
		gameOver()

	if x+BALL_RADIUS > xloc and y+BALL_RADIUS > ysize+OBSTACLE_GAP and x-15 < xsize+xloc:
		# gameOver()
		obstacle_speed = 0
		y_speed = 0
		gameOver()

	if xloc < -80:
		xloc = 700
		ysize = randint(50, 300)

	if x > xloc and x < xloc+3:
		score += 1


	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
