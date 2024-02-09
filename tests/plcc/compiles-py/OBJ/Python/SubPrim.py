#SubPrim:top#
#SubPrim:import#

# <prim>:SubPrim ::= SUBOP
class SubPrim(Prim):

    __className = "SubPrim"
    __ruleString =
        "<prim>:SubPrim ::= SUBOP"
    

    def __init__(self, ):
        #SubPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:SubPrim", scn.lno)
                scn$.match(Token.Match.SUBOP, trace$);
        return new SubPrim();

    #SubPrim#
        