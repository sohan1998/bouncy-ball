
import sys, os
import pygame
from random import randint
file = open("pygame.txt", "a")
e = input("Enter username: ")
file.write(e + " ")
file.close()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
OBSTACLE_GAP = 175
BALL_RADIUS = 20
i=2
pygame.init()

SCREEN_DIMENSIONS = screenX, screenY = (700, 500)
FPS = 60


screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Bouncy Ball")

clock = pygame.time.Clock()


def ball(x,y):
	pygame.draw.circle(screen, BLACK, [x,y], BALL_RADIUS)

def gameOver():
	#if i is not 0:
	file=open("pygame.txt","a")
	file.write(str(score)+"\n")
	file.close()
	#file.write("\n")
	file=open("pygame.txt","r")
	#else:
	yy=200
	font1 = pygame.font.SysFont(None, 50)
	font2 = pygame.font.SysFont(None, 30)
	text = font1.render("GAME OVER", True, RED)
	screen.blit(text, [300, 100])
	t = font1.render("Previous Players", True, BLACK)
	screen.blit(t, [300, 150])
	

	for line in file:
		i = line.split(' ')
		j=i[1]
		k=j[0:len(j)-1]
		text = font2.render(i[0]+"  "+k, True, BLACK)
		screen.blit(text, [300, yy])
		yy+=20
	for event in pygame.event.get():
	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print("BB")
				pygame.quit()
				sys.exit()

def obstacle(xloc, yloc, xsize, ysize):
	pygame.draw.rect(screen, GREEN, [xloc, yloc, xsize,ysize])
	pygame.draw.rect(screen, GREEN, [xloc, int(yloc + ysize + OBSTACLE_GAP), xsize, ysize + screenY])


def Score(score):
	font = pygame.font.SysFont(None, 35)
	text = font.render("Score :  " + str(score), True, BLACK)
	screen.blit(text, [10, 10])
	text2 = font.render("Lives :  " + str(i+1), True, BLACK)
	screen.blit(text2, [10, 30])
j=1
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

while j is not 0:
	keyPressed = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT or keyPressed[pygame.K_ESCAPE]:
			#print("CC")
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# print("QQQQ")
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
		if i is not 0:
			x = screenX//2
			y = screenY//2
			ball(x,y)
			i-=1
			y_speed=0
			xloc = 700
			yloc = 0
			xsize = 70
			ysize = randint(50, 300)
			obstacle_speed = 2
		else:
			y_speed=0
			obstacle_speed=0
			gameOver()
			j=0

	if x+BALL_RADIUS > xloc and y-BALL_RADIUS < ysize and x-15 < xsize+xloc:
		# gameOver()
		if i is not 0:
			x = screenX//2
			y = screenY//2
			ball(x,y)
			i-=1
			y_speed=0
			xloc = 700
			yloc = 0
			xsize = 70
			ysize = randint(50, 300)
			obstacle_speed = 2
		else:
			y_speed=0
			obstacle_speed=0
			gameOver()
			j=0

	if x+BALL_RADIUS > xloc and y+BALL_RADIUS > ysize+OBSTACLE_GAP and x-15 < xsize+xloc:
		# gameOver()
		if i is not 0:
			x = screenX//2
			y = screenY//2
			ball(x,y)
			i-=1
			y_speed=0
			xloc = 700
			yloc = 0
			xsize = 70
			ysize = randint(50, 300)
			obstacle_speed = 2
		else:
			y_speed=0
			obstacle_speed=0
			gameOver()
			j=0
			
	if xloc < -80:
		xloc = 700
		ysize = randint(50, 300)

	if x > xloc and x < xloc+3:
		#if i is not 0:
			score += 1


	pygame.display.flip()
	clock.tick(FPS)
#pygame.time.delay(3000)

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
pygame.quit()