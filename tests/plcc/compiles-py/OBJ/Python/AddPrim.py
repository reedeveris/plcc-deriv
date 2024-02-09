#AddPrim:top#
#AddPrim:import#

# <prim>:AddPrim ::= ADDOP
class AddPrim(Prim):

    __className = "AddPrim"
    __ruleString =
        "<prim>:AddPrim ::= ADDOP"
    

    def __init__(self, ):
        #AddPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:AddPrim", scn.lno)
                scn$.match(Token.Match.ADDOP, trace$);
        return new AddPrim();

    #AddPrim#
        