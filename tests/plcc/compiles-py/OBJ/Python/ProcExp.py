#ProcExp:top#
#ProcExp:import#

# <exp>:ProcExp ::= <proc>
class ProcExp(Exp):

    __className = "ProcExp"
    __ruleString =
        "<exp>:ProcExp ::= <proc>"
    proc = None

    def __init__(self, proc):
        #ProcExp:init#
        self.proc = proc

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:ProcExp", scn.lno)
                Proc proc = Proc.parse(scn$, trace$);
        return new ProcExp(proc);

    #ProcExp#
        