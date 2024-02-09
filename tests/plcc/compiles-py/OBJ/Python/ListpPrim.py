#ListpPrim:top#
#ListpPrim:import#

# <prim>:ListpPrim ::= LISTP
class ListpPrim(Prim):

    __className = "ListpPrim"
    __ruleString =
        "<prim>:ListpPrim ::= LISTP"
    

    def __init__(self, ):
        #ListpPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:ListpPrim", scn.lno)
                scn$.match(Token.Match.LISTP, trace$);
        return new ListpPrim();

    #ListpPrim#
        