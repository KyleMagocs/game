import sys, pygame
from twisted.internet.task import LoopingCall
from client import *
import os

size = width, height = 800, 600
pygame.init()
mypath = os.path.dirname( os.path.realpath( __file__ ) )
imagePath = mypath + "/images/player.png"
player = pygame.image.load(imagePath)
black = 0, 0, 0
screen = pygame.display.set_mode(size)
playerRect = player.get_rect()
speed = [4,4]
    
def main():    
    FPS = 30.0
    tick = LoopingCall(game_tick)
    tick.start(1/FPS)

    factor = ClientFactory()
    #reactor.connectTCP('localhost', 8123, factory)
    reactor.run()
    pygame.QUIT
    
def game_tick():
    global size, player, screen, playerRect,speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()
    playerRect = playerRect.move(speed) 

    if playerRect.left < 0 or playerRect.right > width:
        speed[0] = -speed[0]
    if playerRect.top < 0 or playerRect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(player,playerRect)
    pygame.display.flip()

if __name__ == '__main__':
    main()
