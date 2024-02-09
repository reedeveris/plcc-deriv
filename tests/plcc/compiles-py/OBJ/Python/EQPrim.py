#EQPrim:top#
#EQPrim:import#

# <prim>:EQPrim ::= EQP
class EQPrim(Prim):

    __className = "EQPrim"
    __ruleString =
        "<prim>:EQPrim ::= EQP"
    

    def __init__(self, ):
        #EQPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:EQPrim", scn.lno)
                scn$.match(Token.Match.EQP, trace$);
        return new EQPrim();

    #EQPrim#
        