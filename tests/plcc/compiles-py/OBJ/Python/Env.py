
class Env:

    def initEnv():
        # an environment with an empty local environment
        return EnvNode(Bindings(), EnvNull())

    def applyEnvRef(sym):
        pass
    def replaceBindings(bindings):
        pass
    def add(b):
        pass
    def addFirst(b):
        pass

    def applyEnv(sym):
        return applyEnvRef(sym).deRef()

    def applyEnvRef(tok):
        return applyEnvRef(tok.toString())

    def applyEnv(tok):
        return applyEnv(tok.toString())

    def extendEnvRef(self, bindings):
        return EnvNode(bindings, self)

    def toString(n):
        pass

