#BangAtExp:top#
#BangAtExp:import#

# <exp>:BangAtExp ::= BANGAT
class BangAtExp(Exp):

    __className = "BangAtExp"
    __ruleString =
        "<exp>:BangAtExp ::= BANGAT"
    

    def __init__(self, ):
        #BangAtExp:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:BangAtExp", scn.lno)
                scn$.match(Token.Match.BANGAT, trace$);
        return new BangAtExp();

    #BangAtExp#
        