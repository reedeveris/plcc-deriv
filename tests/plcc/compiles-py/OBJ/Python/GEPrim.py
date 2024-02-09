#GEPrim:top#
#GEPrim:import#

# <prim>:GEPrim ::= GEP
class GEPrim(Prim):

    __className = "GEPrim"
    __ruleString =
        "<prim>:GEPrim ::= GEP"
    

    def __init__(self, ):
        #GEPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:GEPrim", scn.lno)
                scn$.match(Token.Match.GEP, trace$);
        return new GEPrim();

    #GEPrim#
        