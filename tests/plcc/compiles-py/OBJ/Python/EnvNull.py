
class EnvNull(Env):

    // create an environment
    def __init__(self):
        pass

    // find the Ref corresponding to a given id
    def applyEnvRef(sym):
        raise RuntimeException("no binding for "+sym)

    def replaceBindings(bindings):
        raise RuntimeException("no bindings to replace")

    def add(b):
        raise RuntimeException("no bindings to add to")

    def addFirst(b):
        raise RuntimeException("no bindings to add to")

    def toString(n):
        return n + ":\n"

    def toString():
        return "\n"

