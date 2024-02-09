
class ValRORef(Ref):

    val = None

    def __init__(self, val):
        self.val = val

    def deRef(self):
        return self.val

    def setRORef(self, v):
        self.val = v

