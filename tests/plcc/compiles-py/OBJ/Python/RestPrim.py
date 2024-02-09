#RestPrim:top#
#RestPrim:import#

# <prim>:RestPrim ::= RESTOP
class RestPrim(Prim):

    __className = "RestPrim"
    __ruleString =
        "<prim>:RestPrim ::= RESTOP"
    

    def __init__(self, ):
        #RestPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:RestPrim", scn.lno)
                scn$.match(Token.Match.RESTOP, trace$);
        return new RestPrim();

    #RestPrim#
        