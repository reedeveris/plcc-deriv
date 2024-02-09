
class ProcVal(Val):

    formals = None
    nargs = None
    body = None
    env = None

    def __init__(self, formals, body, env):
        self.formals = formals
        self.nargs = formals.varList.size()
        self.body = body
        self.env = env

    def apply(valList):
        if valList.size() != nargs
            raise RuntimeException("formals/arguments number mismatch")
        refList = Ref.valsToRefs(valList)
        bindings = Bindings(formals.varList, refList)
        nenv = env.extendEnvRef(bindings)
        return body.eval(nenv)

    def procVal(self):
        return self

    def env():
        return env

    def toString():
        ret = "proc("
        sep = ""
        for t in formals.varList:
            s = t.toString()
            ret += sep + s
            sep = ","
        ret += ")"
        return ret

