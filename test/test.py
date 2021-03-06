import sys, pygame
from Client import * 
from twisted.internet.task import LoopingCall
import sys, pygame

size = width, height = 320, 240
speed = [4, 3]
black = 0, 0, 0
pygame.init()
ball = pygame.image.load("ball.gif")
screen = pygame.display.set_mode(size)
ballrect = ball.get_rect()

def game_tick():
	global ballrect, speed
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()
	#print ballrect.left
	#print ballrect.top
	
def main():
	stdio.StandardIO(EchoClient())
	#DESIRED_FPS = 30.0 # 30 frames per second

	tick = LoopingCall(game_tick)
	tick.start(1/30)	
	# Set up a looping call every 1/30th of a second to run your game tick

	# Set up anything else twisted here, like listening sockets
	factory = EchoClientFactory()
	reactor.connectTCP('localhost', 8123, factory)
	reactor.run()


	
if __name__ == '__main__':
    main()


