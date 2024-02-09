#ObjectpPrim:top#
#ObjectpPrim:import#

# <prim>:ObjectpPrim ::= OBJECTP
class ObjectpPrim(Prim):

    __className = "ObjectpPrim"
    __ruleString =
        "<prim>:ObjectpPrim ::= OBJECTP"
    

    def __init__(self, ):
        #ObjectpPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:ObjectpPrim", scn.lno)
                scn$.match(Token.Match.OBJECTP, trace$);
        return new ObjectpPrim();

    #ObjectpPrim#
        