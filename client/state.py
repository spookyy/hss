class State:
    def __init__(self):
        pass
    def action(self, event):
        pass
    
class NonState(State):
    @staticmethod
    def action(role):
        print "This is NonState"
        role.set_state(StartState())
        
class StartState(State):
    @staticmethod
    def action(role):
        print "This is StartState"
        role.set_state(JudgeState())

class JudgeState(State):
    @staticmethod
    def action(role):
        print "This is JudgeState"
        role.set_state(DrawState())
        
class DrawState(State):
    @staticmethod
    def action(role):
        print "This is DrawState"
        role.set_state(DealState())
        
class DealState(State):
    @staticmethod
    def action(role):
        print "This is DealState"
        role.set_state(DiscardState())
        
class DiscardState(State):
    @staticmethod
    def action(role):
        print "This is DiscardState"
        role.set_state(EndState())
 
class EndState(State):
    @staticmethod
    def action(role):
        print "This is EndState"
        role.set_state(NonState())
               