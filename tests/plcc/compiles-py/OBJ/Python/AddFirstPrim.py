#AddFirstPrim:top#
#AddFirstPrim:import#

# <prim>:AddFirstPrim ::= ADDFIRSTOP
class AddFirstPrim(Prim):

    __className = "AddFirstPrim"
    __ruleString =
        "<prim>:AddFirstPrim ::= ADDFIRSTOP"
    

    def __init__(self, ):
        #AddFirstPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:AddFirstPrim", scn.lno)
                scn$.match(Token.Match.ADDFIRSTOP, trace$);
        return new AddFirstPrim();

    #AddFirstPrim#
        