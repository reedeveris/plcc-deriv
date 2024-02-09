
class StdClass(ClassVal):

    superClass = None  // an EnvClass (top-level) or a StdClass
    staticBindings = None
    fields = None
    methods = None
    staticEnv = None

    def __init__(self,
            env,             // the environment where self class is created
            superClass, // evaluated by ClassExp
            statics,     // static variable definitions
            fields,       // field declarations
            methods):  // method definitions
        self.superClass = superClass
        self.fields = fields
        self.methods = methods
	// my static environment starts with the superclass environment
        self.staticEnv = superClass.env()
        // the staticBindings field is used to create instances of self class
        self.staticBindings = new Bindings()
        self.staticEnv = staticEnv.extendEnvRef(staticBindings)
        // initially create bindings for these static symbols ...
        staticBindings.append("!@", ValRef(ObjectVal(env))) // not a var
        staticBindings.append("myclass", ValRef(self))
        staticBindings.append("superclass", ValRef(superClass))
        // The static RHS expressions are evaluated in the modified
        // staticEnv that includes the bindings for myclass, superclass.
        // New static bindings are added as they are created,
        // as in top-level defines
        statics.addStaticBindings(staticBindings, staticEnv)

    def env(self):
        return self.staticEnv

    def makeObject(self, objRef):
        // System.err.println("... in makeObject ...");
        // create the parent object first (recursively)
        parent = self.superClass.makeObject(objRef)

        // self object's environment extends the parent object's environment
        env = parent.objectEnv

        // add self class's static bindings (including those for myclass, etc)
        env = env.extendEnvRef(staticBindings)

        // the fields come next
        fieldBindings = Bindings()
        env = env.extendEnvRef(fieldBindings)
        // bind all of self object's instance fields to nil
        for t in fields.varList:
            s = t.toString()
            fieldBindings.append(s, ValRef(Val.nil))
        // bind all self object's methods as in letrec
        // don't add any bindings if there are no method declarations
        if methods.varList.size() > 0:
            methodDecls = LetrecDecls(methods.varList, methods.procList)
            env = methodDecls.addBindings(env)

        // create the object and return it
        // bind 'super' field to the parent object
        fieldBindings.append("super", ValRef(parent)) // parent object
        // bind 'self' field to the base object being created
        // (to speed up lookups)
        fieldBindings.append("self", objRef) // deep
        // bind 'self' field to self object environment
        objectVal = ObjectVal(env)
        fieldBindings.append("self", ValRef(objectVal)) // shallow
        return objectVal

    def toString():
        return "class"

