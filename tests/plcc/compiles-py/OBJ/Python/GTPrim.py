#GTPrim:top#
#GTPrim:import#

# <prim>:GTPrim ::= GTP
class GTPrim(Prim):

    __className = "GTPrim"
    __ruleString =
        "<prim>:GTPrim ::= GTP"
    

    def __init__(self, ):
        #GTPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:GTPrim", scn.lno)
                scn$.match(Token.Match.GTP, trace$);
        return new GTPrim();

    #GTPrim#
        