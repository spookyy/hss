import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import cocos
class MainScene(cocos.scene.Scene):
	def __init__(self, sock):
		super(MainScene, self).__init__(Room(self,sock))
		self.director = cocos.director.Director()
		self.director.init()
		self.director.run(self)
	
	def addChild(self, child, z, name):
		self.add(child, z=z, name=name)

	def removeChild(self, child):
		self.remove(child)





