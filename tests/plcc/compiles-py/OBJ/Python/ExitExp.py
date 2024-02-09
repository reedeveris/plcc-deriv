#ExitExp:top#
#ExitExp:import#

# <exp>:ExitExp ::= EXIT
class ExitExp(Exp):

    __className = "ExitExp"
    __ruleString =
        "<exp>:ExitExp ::= EXIT"
    

    def __init__(self, ):
        #ExitExp:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:ExitExp", scn.lno)
                scn$.match(Token.Match.EXIT, trace$);
        return new ExitExp();

    #ExitExp#
        