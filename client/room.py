import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import cocos

class Room(cocos.layer.Layer):
    def __init__(self, sock):
        super(Room, self).__init__()
        
        self.sock = sock
        
        label = cocos.text.Label('Hello, world',
             font_name='liberationmono',
             font_size=32,
             anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)
    
    
    