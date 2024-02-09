
class Bindings:

    bindingList = None

    // create an empty list of bindings
    def __init__(self):
        self.bindingList = []

    def __init__(self, bindingList):
        self.bindingList = bindingList

    // idList is a list of Tokens/Strings
    // refList is a list of Refs
    def __init__(self, idList, refList):
        self.bindingList = []
        idIterator = iter(idList)
        refIterator = iter(refList)
        while next(idIterator) not None:
            id = next(idIterator).toString()
            ref = next(refIterator)
            self.bindingList.append(Binding(id, ref))

    def add(self, s, r):
        self.bindingList.append(Binding(s, r))

    def addFirst(self, b):
        self.bindingList.insert(0,b)

    def add(self, b):
        self.bindingList.add(b)

    def size(self):
        return self.bindingList.size()

    def toString(self):
        s = ""
        for b in self.bindingList:
            s += " " + b
        return s

