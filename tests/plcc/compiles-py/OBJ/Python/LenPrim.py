#LenPrim:top#
#LenPrim:import#

# <prim>:LenPrim ::= LENOP
class LenPrim(Prim):

    __className = "LenPrim"
    __ruleString =
        "<prim>:LenPrim ::= LENOP"
    

    def __init__(self, ):
        #LenPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:LenPrim", scn.lno)
                scn$.match(Token.Match.LENOP, trace$);
        return new LenPrim();

    #LenPrim#
        