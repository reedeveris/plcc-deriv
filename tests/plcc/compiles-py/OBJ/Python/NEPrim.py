#NEPrim:top#
#NEPrim:import#

# <prim>:NEPrim ::= NEP
class NEPrim(Prim):

    __className = "NEPrim"
    __ruleString =
        "<prim>:NEPrim ::= NEP"
    

    def __init__(self, ):
        #NEPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:NEPrim", scn.lno)
                scn$.match(Token.Match.NEP, trace$);
        return new NEPrim();

    #NEPrim#
        