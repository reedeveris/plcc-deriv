#FirstPrim:top#
#FirstPrim:import#

# <prim>:FirstPrim ::= FIRSTOP
class FirstPrim(Prim):

    __className = "FirstPrim"
    __ruleString =
        "<prim>:FirstPrim ::= FIRSTOP"
    

    def __init__(self, ):
        #FirstPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:FirstPrim", scn.lno)
                scn$.match(Token.Match.FIRSTOP, trace$);
        return new FirstPrim();

    #FirstPrim#
        