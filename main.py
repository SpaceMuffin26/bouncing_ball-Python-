#saba diasamidze

#to add:
#	textures
#	outlines
#	velocity


#logic:

#modules
import sys, pygame
pygame.init()

#variables and such
size = width, height = 320, 240
speed = [2, 2]
color_background = (20, 20, 25) #darkgreen
color_ball = (255, 40, 40) #light red
screen = pygame.display.set_mode((1920, 1080))
running = True
ball_radius = 40


#places the ball in the middle of the screen
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#runs the game untill player pressed the exit button
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
            
    #sets backround color
	screen.fill(color_background)        
    
    #sets ball with all its stats
	ball = pygame.draw.circle(screen, color_ball, ball_pos, ball_radius)
	
	#adds gravity
	ball_pos.y += speed[0]
	
	#bounces, doesnt work
	if ball_pos.y - ball_radius < 0 or ball_pos.y + ball_radius > screen.get_height():
		speed[0] = -speed[0]
	
	#redraws the game frame
	pygame.display.flip()
