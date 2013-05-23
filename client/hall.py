import pygame
from pygame.locals import *


class Hall:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    
    
    def __init__(self):
        # Initial pygame
        
        pygame.init()
        pygame.display.set_caption("HEI SHEN SHA")
		self.screen = pygame.display.set_mode((640, 480), 0, 32)
        self.screen.fill((0, 0, 0))
		font = pygame.font.SysFont("Arial",16)
        self.screen.blit(font, (0,96) 
        
        self.textrect1 = Rect(0, 0, 640, 96)
        self.textrect2 = Rect(0, 96, 640, 96)
        self.textrect3 = Rect(0, 192, 640, 96)
        self.textrect4 = Rect(0, 288, 640, 96)
        self.textrect5 = Rect(0, 394, 640, 96)
        self.area = Rect(0, 192, 640, 480)
        
        self.selectedColor = Hall.BLUE
        
        
        
    def run(self):
        # Run the event loop
        self.loop()
        # Close the pygame window
        pygame.quit()
    
    def loop(self):
        Exit = False
        while not Exit:
            Exit = self.handleEvents()
            self.draw()
            
    def handleEvents(self):
        Exit = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                Exit = True
            elif event.type == KEYDOWN:
                Exit = True
            elif event.type == MOUSEBUTTONDOWN:
                self.handleMouseDown(pygame.mouse.get_pos())
        return Exit
    
    def handleMouseDown(self, (x,y)):
        print x,y
        if(self.textrect1.collidepoint(x,y)):
            self.selectedColor = Hall.BLUE
            print "rect1"
        elif (self.textrect2.collidepoint(x,y)):
            self.selectedColor = Hall.RED
            print "rect2"
        elif (self.textrect3.collidepoint(x,y)):
            print "rect3"
        elif (self.textrect4.collidepoint(x,y)):
            print "rect4"
        else:
            print "rect5"    
    
    def draw(self):
        #self.makeText("reset", (255,125,125))
        pygame.draw.rect(
                         self.screen,
                         Hall.BLUE, 
                         self.textrect1
                         )
        pygame.draw.rect(
                         self.screen,
                         Hall.RED,
                         self.textrect2
                         )
        
        pygame.draw.rect(
                         self.screen,
                         self.selectedColor,
                         self.area
                         )
        pygame.display.update()
        
    def makeText(self, text, color):
        font = pygame.font.SysFont('arial', 6)
        textSurf = BASICFONT.render(text, True, color)
        self.screen.blit(textSurf,(320, 240))


Hall().run()
    
    
    
    
    
