import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pyglet import image, font
from pyglet.gl import *
from pyglet.window import key

import cocos
from cocos.sprite import Sprite

from pygame.locals import *


class Room(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self, sock):
        super(Room, self).__init__()
        
        self.sock = sock
        
		self.image1.anchor_x = self.image1.width/2
        self.image1.anchor_y = self.image1.height/2
        sprite1 = Sprite(self.image1)
        self.add(sprite1, z=0, name="qiuqiu")
        sprite1.position = 220, 240
        
        self.image2 = pyglet.resource.image('heishen.jpg')
        self.image2.anchor_x = self.image2.width/2
        self.image2.anchor_y = self.image2.height/2
        sprite2 = Sprite(self.image2)
        self.add(sprite2, z=0, name="heishen")
        sprite2.position = 420, 240
        
        label = cocos.text.Label('Pick one? Click He or She!',
            font_name='liberationmono',
            font_size=16,
            anchor_x='center', anchor_y='center')

        label.position = 320, 80
        self.add( label )
        
        
        
    def on_mouse_press(self, x, y, mouse, modifiers):
        """This function is called when mouse is pressed.
        """
        print x, y, mouse, modifiers
        rect1 = Rect(140, 120, 160, 240)
        rect2 = Rect(340, 120, 160, 240)
        
        if(rect1.collidepoint(x,y)):
            print "left area clicked"
        elif(rect2.collidepoint(x,y)):
            print "right area clicked"

    def button_pressed(self):
        print "print_text"

class GameLayer(cocos.layer.ColorLayer):
	is_event_handler = True
	def __init__(self, sock):
		super(GameLayer,self).__init__(124,234,23, 128)
		
		self.sock = sock

	def on_mouse_pressed(self, x, y, mouse, modifiers):
		"""
			This function is called when mouse is pressed,
			Used to handle click event
		"""
		rect = Rect(0, 0, 640, 480)
		
		if(rect.collidepoint(x,y)):
			print "GameLayer is clicked"
		else:
			pass
	
		








    
    
