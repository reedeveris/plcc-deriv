#MulPrim:top#
#MulPrim:import#

# <prim>:MulPrim ::= MULOP
class MulPrim(Prim):

    __className = "MulPrim"
    __ruleString =
        "<prim>:MulPrim ::= MULOP"
    

    def __init__(self, ):
        #MulPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:MulPrim", scn.lno)
                scn$.match(Token.Match.MULOP, trace$);
        return new MulPrim();

    #MulPrim#
        