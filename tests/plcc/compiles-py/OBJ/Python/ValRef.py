
class ValRef(Ref):

    val = None

    def __init__(self, val):
        self.val = val

    def deRef(self):
        return self.val

    def setRef(self, v):
        self.val = v

