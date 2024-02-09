class Binding:

    id = None
    ref = None

    def __init__(self, id, ref):
        self.id = id
        self.ref = ref

    def toString():
        return "[" + id + "->" + ref.deRef().toString() + "]"

