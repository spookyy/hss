import pygame
from pygame.locals import *


class Hall:
    def __init__(self,sock):
        # Initial pygame
        pygame.init()
        pygame.display.set_caption("HEI SHEN SHA")
        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        self.screen.fill((0, 125, 125))
                
        self.Exit = False
        
        self.textrect1 = Rect(0, 0, 640, 96)
        self.textrect2 = Rect(0, 96, 640, 96)
        self.textrect3 = Rect(0, 192, 640, 96)
        self.textrect4 = Rect(0, 288, 640, 96)
        self.textrect5 = Rect(0, 394, 640, 96)

        self.text = ["room room_id_1 ROOM A 0/2 not_ready",
                     "room room_id_2 ROOM B 0/2 not_ready",
                     "room room_id_3 ROOM C 0/2 not_ready",
                     "room room_id_4 ROOM D 0/2 not_ready",
                     "room room_id_5 ROOM E 0/2 not_ready"]
        self.sock = sock
        for i in range(0,5):
            data = self.sock.recv(33)
            self.text[i] = data
            print i, data
    def run(self):
        # Run the event loop
        self.loop()
        # Close the pygame window
        pygame.quit()
    
    def loop(self):
        while not self.Exit:
            self.handleEvents()
            self.draw()
            
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.Exit = True
            elif event.type == KEYDOWN:
                self.Exit = True
            elif event.type == MOUSEBUTTONDOWN:
                self.handleMouseDown(pygame.mouse.get_pos())
    
    def handleMouseDown(self, (x,y)):
        if(self.textrect1.collidepoint(x,y)):
            self.sock.send(u"room_id_1")
            data = self.sock.recv(3)
            if unicode(data) == "ok":
                self.Exit = True
            elif unicode(data) == "nok":
                print "room is full, can't get into the room"
                self.Exit = True
        elif (self.textrect2.collidepoint(x,y)):
            self.sock.send(u"room_id_2")
            data = self.sock.recv(3)
            if unicode(data) == "ok":
                self.Exit = True
            elif unicode(data) == "nok":
                print "room is full, can't get into the room"
                self.Exit = True
        elif (self.textrect3.collidepoint(x,y)):
            self.sock.send(u"room_id_3")
            data = self.sock.recv(3)
            if unicode(data) == "ok":
                self.Exit = True
            elif unicode(data) == "nok":
                print "room is full, can't get into the room"
                self.Exit = True
        elif (self.textrect4.collidepoint(x,y)):
            self.sock.send(u"room_id_4")
            data = self.sock.recv(3)
            if unicode(data) == "ok":
                self.Exit = True
            elif unicode(data) == "nok":
                print "room is full, can't get into the room"
                self.Exit = True
        else:
            self.sock.send(u"room_id_5")
            data = self.sock.recv(3)
            if unicode(data) == "ok":
                self.Exit = True
            elif unicode(data) == "nok":
                print "can't get into the room"
                self.Exit = True
    
    def draw(self):
        self.makeText( self.text[0], (255,125,125), self.textrect1)
        pygame.draw.line(self.screen, (0,0,0), (0,96), (640, 96))
        self.makeText( self.text[1], (255,125,125), self.textrect2)
        pygame.draw.line(self.screen, (0,0,0), (0,192), (640, 192))
        self.makeText( self.text[2], (255,125,125), self.textrect3)
        pygame.draw.line(self.screen, (0,0,0), (0,288), (640, 288))
        self.makeText( self.text[3], (255,125,125), self.textrect4)
        pygame.draw.line(self.screen, (0,0,0), (0,384), (640, 384))
        self.makeText( self.text[4], (255,125,125), self.textrect5)
        pygame.display.update()
        
    def makeText(self, text, color, rect):
        font = pygame.font.SysFont('liberationmono', 16)
        textSurf = font.render(text, True, color)
        self.screen.blit(textSurf,rect)

    
    
    
    
