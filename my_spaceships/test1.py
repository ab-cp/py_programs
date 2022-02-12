# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Run until the user asks to quit
running = True
while running:

	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Fill the backround with white
	screen.fill((20, 255, 234))

	# Draw a solid blue circle in the center

	pygame.draw.circle(screen, (139, 69, 19), (250, 250), 75)
	pygame.draw.circle(screen, (0, 25, 255), (100, 100), 75)
	pygame.draw.rect(screen, (20, 255, 234), (250, 63, 400, 500))
	

	# Flip the display
	pygame.display.flip()

# Done! Time to quit.

pygame.quit()
