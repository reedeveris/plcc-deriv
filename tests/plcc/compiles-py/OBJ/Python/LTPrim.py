#LTPrim:top#
#LTPrim:import#

# <prim>:LTPrim ::= LTP
class LTPrim(Prim):

    __className = "LTPrim"
    __ruleString =
        "<prim>:LTPrim ::= LTP"
    

    def __init__(self, ):
        #LTPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:LTPrim", scn.lno)
                scn$.match(Token.Match.LTP, trace$);
        return new LTPrim();

    #LTPrim#
        