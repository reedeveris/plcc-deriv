#NilExp:top#
#NilExp:import#

# <exp>:NilExp ::= NIL
class NilExp(Exp):

    __className = "NilExp"
    __ruleString =
        "<exp>:NilExp ::= NIL"
    

    def __init__(self, ):
        #NilExp:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:NilExp", scn.lno)
                scn$.match(Token.Match.NIL, trace$);
        return new NilExp();

    #NilExp#
        