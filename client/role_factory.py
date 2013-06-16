## this is a factory that create any player whoever you want
## implemented in simple factory pattern
from heishen import *
from qiumochuang import *
from state import *

class RoleFactory:
    
    @staticmethod
    def create(which_role):
        if which_role == "heishen":
            return Heishen((1,2,3,4,5,6,7,8,9,NonState()))
        elif which_role == "qiumochuang":
            return Qiumochuang((1,2,3,4,5,6,7,8,9,NonState))
        else:
            return None
        