#DivPrim:top#
#DivPrim:import#

# <prim>:DivPrim ::= DIVOP
class DivPrim(Prim):

    __className = "DivPrim"
    __ruleString =
        "<prim>:DivPrim ::= DIVOP"
    

    def __init__(self, ):
        #DivPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:DivPrim", scn.lno)
                scn$.match(Token.Match.DIVOP, trace$);
        return new DivPrim();

    #DivPrim#
        