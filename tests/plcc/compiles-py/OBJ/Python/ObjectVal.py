
class ObjectVal(Val):

    objectEnv = None     // self object's environment

    def __init__(self, env):
        self.objectEnv = env

    def objectVal(self):
        return self

    def isObject():
        return True

    def env(self):
        return self.objectEnv

    def toString():
        return "object"

