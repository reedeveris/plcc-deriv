#LEPrim:top#
#LEPrim:import#

# <prim>:LEPrim ::= LEP
class LEPrim(Prim):

    __className = "LEPrim"
    __ruleString =
        "<prim>:LEPrim ::= LEP"
    

    def __init__(self, ):
        #LEPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:LEPrim", scn.lno)
                scn$.match(Token.Match.LEP, trace$);
        return new LEPrim();

    #LEPrim#
        