import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import cocos

class Room(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self, scene, sock):
        super(Room, self).__init__()
        
        self.sock = sock
        self.scene = scene

        label = cocos.text.Label('Hello, world',
             font_name='liberationmono',
             font_size=32,
             anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)
        
    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which  
        'modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        """
        
        self.keys_pressed.add(key)
        sefl.print_test()

    def print_text(self):
        print "key pressed"


    
    
