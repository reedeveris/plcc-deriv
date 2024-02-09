#Add1Prim:top#
#Add1Prim:import#

# <prim>:Add1Prim ::= ADD1OP
class Add1Prim(Prim):

    __className = "Add1Prim"
    __ruleString =
        "<prim>:Add1Prim ::= ADD1OP"
    

    def __init__(self, ):
        #Add1Prim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:Add1Prim", scn.lno)
                scn$.match(Token.Match.ADD1OP, trace$);
        return new Add1Prim();

    #Add1Prim#
        