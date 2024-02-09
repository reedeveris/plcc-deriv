
class Ref:

    def valsToRefs(valList):
        refList = []
        for v in valList:
            refList.append(ValRef(v))
        return refList

    def deRef():
        pass
    def setRef(v):
        raise RuntimeException("cannot modify a read-only reference")

