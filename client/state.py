class State:
    def __init__(self):
        pass
    def action(self, event):
        pass
    
class NonState(State):
    def action(self, role):
        print "this is nonstate"
        role.set_state(StartState())
        
class StartState(State):
    def action(self, role):
        print "this is startstate"
        role.set_state(JudgeState())

class JudgeState(State):
    def action(self, role):
        print "this is judgestate"
        role.set_state(DrawState())
        
class DrawState(State):
    def action(self, role):
        print "this is drawstate"
        role.set_state(DealState())
        
class DealState(State):
    def action(self, role):
        print "this is dealstate"
        role.set_state(DiscardState())
        
class DiscardState(State):
    def action(self, role):
        print "this is discardstate"
        role.set_state(EndState())
 
class EndState(State):
    def action(self, role):
        print "this is endstate"
        role.set_state(NonState())
               
