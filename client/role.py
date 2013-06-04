## this is father class of plyers
class Role:
    def __init__(self, role_attr):
        (Id, name, image_id, hp, ev, attack, defence, h_rate, evd, state) = role_attr
        self.Id = Id
        self.name = name
        self.image_id = image_id
        self.hp = hp
        self.ev = ev 
        self.attack = attack
        self.defence = defence
        self.h_rate = h_rate
        self.evd = evd
        
        ## 
        self.state = state
        
    def action(self):
        pass
    def set_state(self):
        pass