#Eval:top#
#Eval:import#

# <program>:Eval ::= <exp>
class Eval(Program):

    __className = "Eval"
    __ruleString =
        "<program>:Eval ::= <exp>"
    exp = None

    def __init__(self, exp):
        #Eval:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<program>:Eval", scn.lno)
                Exp exp = Exp.parse(scn$, trace$);
        return new Eval(exp);

    #Eval#
        