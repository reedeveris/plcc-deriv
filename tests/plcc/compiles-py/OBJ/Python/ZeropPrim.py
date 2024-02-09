#ZeropPrim:top#
#ZeropPrim:import#

# <prim>:ZeropPrim ::= ZEROP
class ZeropPrim(Prim):

    __className = "ZeropPrim"
    __ruleString =
        "<prim>:ZeropPrim ::= ZEROP"
    

    def __init__(self, ):
        #ZeropPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:ZeropPrim", scn.lno)
                scn$.match(Token.Match.ZEROP, trace$);
        return new ZeropPrim();

    #ZeropPrim#
        