
class PLCCException(RuntimeError):
    msg = None

    def __init__(self, pfx, msg):
        super(msg = "%%% " + pfx + ": " + msg)
        self.msg = msg

    def __init__(self, msg):
        self("Runtime error", msg)

    def toString():
        return self.msg

