
class ListNode(ListVal):

    val = None
    listVal = None
    length = None

    def __init__(self, val, listVal):
        self.val = val
        self.listVal = listVal
        self.length = listVal.len() + 1

    def env():
        raise RuntimeException("ListVal: no environment")

    def isList():
	    return True

    def listNode(self):
        return self

    def toString():
        return "[" + self.toString("") + "]"

    def putc():
	    return val.putc() + listVal.putc()

    def toString(sep):
        return sep + val + listVal.toString(",")

    def len(self):
        return self.length

