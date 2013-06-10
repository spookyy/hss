import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pyglet import image, font
from pyglet.gl import *
from pyglet.window import key

import cocos
from cocos.sprite import Sprite

from pygame.locals import *

from cocos.layer import *
from cocos.scene import *
from cocos.director import *


class Room(Layer):
    is_event_handler = True
    def __init__(self, sock):
        super(Room, self).__init__()
        
        self.sock = sock
        
        self.image1 = pyglet.resource.image('qiuqiu.jpg')
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
        rect1 = Rect(140, 120, 160, 240)
        rect2 = Rect(340, 120, 160, 240)
        
        if(rect1.collidepoint(x,y)):
            start_game_with_hero(1)
        elif(rect2.collidepoint(x,y)):
            start_game_with_hero(2)
            

class GameLayer(Layer):
    is_event_handler = True
    def __init__(self, sock):
        super(GameLayer,self).__init__()
        
        self.sock = sock
        
        label = cocos.text.Label('Welcome Player!',
            font_name='liberationmono',
            font_size=32,
            anchor_x='center', anchor_y='center')

        label.position = 320,240
        self.add( label )
        
    def on_mouse_press(self, x, y, mouse, modifiers):
        """
            This function is called when mouse is pressed,
            Used to handle click event
        """, 
        print x, y, mouse
        rect = Rect(0, 0, 640, 480)
        
        if(rect.collidepoint(x,y)):
            print "GameLayer is clicked"
        else:
            pass
        
def start_game_with_hero(hero):
    gameBgLayer = ColorLayer(122, 3, 255, 128)
    gameLayer = GameLayer(123)
    gameScene = Scene(gameBgLayer, gameLayer)
    director.replace(gameScene)
        
if __name__ == "__main__":    
    director.init(width=640, height=480, caption="hei shen sha").set_location(353, 144)
    
    pickBgLayer = ColorLayer(122, 3, 255, 128)
    pickLayer = Room(123)
    pickScene = Scene(pickBgLayer, pickLayer)
    director.run(pickScene)
