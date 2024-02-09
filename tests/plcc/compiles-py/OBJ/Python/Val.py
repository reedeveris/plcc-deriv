
class Val():

    nil = NilVal()
    zero = IntVal(0)
    listNull = ListNull()

    def toArray(valList):
        n = valList.size()
        return valList.toArray(Val[n])

    def apply(self,valList):
        raise RuntimeException(self + ": not a procedure")

    def env(self):
	    raise RuntimeException("<" + self + ">: not an environment")

    def isTrue():
	    return True # everything is true except for an IntVal of zero

    def intVal(self):
        raise RuntimeException(self + ": not an Int")

    def listVal(self):
        raise RuntimeException(self + ": not a List")

    def classVal(self)
        raise RuntimeException(self + ": not a Class")

    def objectVal(self):
        raise RuntimeException(self + ": not an Object")


    def listNode(self):
        raise RuntimeException(self + ": not a nonempty List")

    def isList():
	    return False

    def isObject():
	    return False

    def isClass():
        return False

    def makeObject(self,objRef):
        raise RuntimeException("new " + self + ": not a class")

    def putc(self):
	    return self.toString()

