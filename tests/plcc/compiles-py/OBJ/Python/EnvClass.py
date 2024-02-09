
def EnvClass(ClassVal):

    staticEnv = None

    def __init__(self, env):
        self.staticEnv = env // the environment inherited by all subclasses

    def env(self):
        return self.staticEnv

    // Observe that the environment of objects created with 'new ...'
    // always end up extending the static environment of self class.
    // The 'objRef' reference will eventually be set to the object
    // being created.
    def makeObject(self, objRef):
        // start with the static environment of self class
        env = self.staticEnv
        // add the field binding 'self' to refer to the base object (deep)
        fieldBindings = Bindings()
        env = env.extendEnvRef(fieldBindings) // self object's environment
        fieldBindings.append("self", objRef)                // deep
        return ObjectVal(env)

    def toString():
        // return "class:" + staticEnv.getDepth()
        return "class"

