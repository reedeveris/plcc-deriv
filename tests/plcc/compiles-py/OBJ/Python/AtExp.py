#AtExp:top#
#AtExp:import#

# <exp>:AtExp ::= AT
class AtExp(Exp):

    __className = "AtExp"
    __ruleString =
        "<exp>:AtExp ::= AT"
    

    def __init__(self, ):
        #AtExp:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:AtExp", scn.lno)
                scn$.match(Token.Match.AT, trace$);
        return new AtExp();

    #AtExp#
        