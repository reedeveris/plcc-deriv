#AtAtExp:top#
#AtAtExp:import#

# <exp>:AtAtExp ::= ATAT
class AtAtExp(Exp):

    __className = "AtAtExp"
    __ruleString =
        "<exp>:AtAtExp ::= ATAT"
    

    def __init__(self, ):
        #AtAtExp:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:AtAtExp", scn.lno)
                scn$.match(Token.Match.ATAT, trace$);
        return new AtAtExp();

    #AtAtExp#
        