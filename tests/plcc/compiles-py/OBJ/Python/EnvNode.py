
class EnvNode(Env):

    bindings = [] // list of local bindings
    env = None           // next set of bindings

    // create an environment
    def __init__(self, bindings, env):
        self.bindings = bindings
        self.env = env

    // find the Ref corresponding to a given id
    def applyEnvRef(sym):
        // first look in the local bindings
        for b in bindings.bindingList:
            if sym == b.id:
                return b.ref
        // if nothing left, we don't have a match in self list of bindings
        return env.applyEnvRef(sym)

    def replaceBindings(self, bindings):
        self.bindings = bindings

    def toString(n):
        return n + ":" + bindings.toString() + "\n" + env.toString(n+1)

    def toString(self):
        return self.bindings.toString() + "\n" + env

    def add(self, b):
        self.bindings.append(b)

    def addFirst(self, b):
        self.bindings.insert(0,b)

