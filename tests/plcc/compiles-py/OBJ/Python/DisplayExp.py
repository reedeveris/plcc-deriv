#DisplayExp:top#
#DisplayExp:import#

# <exp>:DisplayExp ::= DISPLAY <exp>
class DisplayExp(Exp):

    __className = "DisplayExp"
    __ruleString =
        "<exp>:DisplayExp ::= DISPLAY <exp>"
    exp = None

    def __init__(self, exp):
        #DisplayExp:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:DisplayExp", scn.lno)
                scn$.match(Token.Match.DISPLAY, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new DisplayExp(exp);

    #DisplayExp#
        