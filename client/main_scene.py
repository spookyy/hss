import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))



import cocos
import room
from cocos.director import *

class MainScene(cocos.scene.Scene):
    def __init__(self, sock):
        super(MainScene, self).__init__(
            room.Room(self,sock))

    def addChild(self, child, z, name):
        self.add(child, z=z, name=name)

    def removeChild(self, child):
        self.remove(child)
        
director.init(width=640, height=480, caption="hei shen sha")
director.run(MainScene(123))
