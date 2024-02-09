#VarExp:top#
#VarExp:import#

# <exp>:VarExp ::= <VAR>
class VarExp(Exp):

    __className = "VarExp"
    __ruleString =
        "<exp>:VarExp ::= <VAR>"
    var = None

    def __init__(self, var):
        #VarExp:init#
        self.var = var

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:VarExp", scn.lno)
                Token var = scn$.match(Token.Match.VAR, trace$);
        return new VarExp(var);

    #VarExp#
        