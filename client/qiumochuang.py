from role import *

class Qiumochuang(Role):
    def __init__(self,role_attr):
        Role.__init__(self,role_attr)
    def action(self):
        self.state.action(self)
    def set_state(self, state):
        self.state = state    