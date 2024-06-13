import pygame
import random
import time

pygame.init()

N=400
Steps=20
r = 10

SW=1000 
SH=600
OBS = 50

screen = pygame.display.set_mode((SW,SH))
pygame.display.set_caption("DotsEnv")
clock = pygame.time.Clock()


Dots = []
for _ in range(N):
	Dots.append([random.uniform(0,SW),random.uniform(0,SH),(random.randint(5,220),random.randint(5,220),random.randint(5,220))])

def isCollision(A,B,r):
	d = (A[0]-B[0])**2 + (A[1]-B[1])**2
	d = d**0.5
	if(d <= 2*r):
		return 1

def print_text(text,x,y):
	img = pygame.font.SysFont("Arial",30).render(text,1,(255,255,255))
	screen.blit(img,(x,y))



run = N
Q = 1
st = time.perf_counter()
while(run*Q):
	
	clock.tick(60)
	screen.fill((0,0,0))
	print_text(f"Dots: {run}",SW-170,SH-100)
	print_text(f"Time: {time.perf_counter()-st}",SW-166,SH-78)

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Q = 0
	
	for dot in Dots:
		pygame.draw.circle(screen,dot[2],(dot[0],dot[1]),r)
	
		dot[0]+= random.uniform(-Steps,Steps)
		dot[1]+= random.uniform(-Steps,Steps)
		

		if(dot[0] < 0+OBS):
			dot[0] = 0+OBS
		
		elif (dot[0] > SW-OBS):
			dot[0] = SW-OBS
		
		elif(dot[1]< 0+OBS):
			dot[1] = 0+OBS
		
		elif (dot[1] > SH-OBS):
			dot[1] = SH-OBS

		for b in Dots:
			if( dot!=b and isCollision(dot,b,r)):
				try:
					Dots.remove(dot)
					Dots.remove(b)
				except:
					pass


	run = len(Dots)
	pygame.display.flip()

et = time.perf_counter()
print(f"N={N} T={et-st}")
pygame.quit()