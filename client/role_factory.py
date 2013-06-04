## this is a factory that create any player whoever you want
## implemented in simple factory pattern
from heishen import *
from qiumochuang import *

class RoleFactory:
    def create(self, which_role):
        if which_role == "heishen":
            return Heishen((1,2,3,4,5,6,7,8,9,10))
        elif which_role == "qiumochuang":
            return Qiumochuang((1,2,3,4,5,6,7,8,9,10))
        else:
            return None
        