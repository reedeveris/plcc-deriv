#ErrorExp:top#
#ErrorExp:import#

# <exp>:ErrorExp ::= ERROR <exp>
class ErrorExp(Exp):

    __className = "ErrorExp"
    __ruleString =
        "<exp>:ErrorExp ::= ERROR <exp>"
    exp = None

    def __init__(self, exp):
        #ErrorExp:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:ErrorExp", scn.lno)
                scn$.match(Token.Match.ERROR, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new ErrorExp(exp);

    #ErrorExp#
        