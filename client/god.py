import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import cocos
import main_scene


class God():
    def __init__(self, sock):
        self.director = cocos.director.Director()
        self.director.init()
        
        self.sock = sock

        self.scene = main_scene.MainScene(sock)

    def run():        
        self.director.run(self.scene)

God(12).run()
