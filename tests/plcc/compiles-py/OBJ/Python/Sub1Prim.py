#Sub1Prim:top#
#Sub1Prim:import#

# <prim>:Sub1Prim ::= SUB1OP
class Sub1Prim(Prim):

    __className = "Sub1Prim"
    __ruleString =
        "<prim>:Sub1Prim ::= SUB1OP"
    

    def __init__(self, ):
        #Sub1Prim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:Sub1Prim", scn.lno)
                scn$.match(Token.Match.SUB1OP, trace$);
        return new Sub1Prim();

    #Sub1Prim#
        