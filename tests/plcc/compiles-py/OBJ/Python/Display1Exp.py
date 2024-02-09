#Display1Exp:top#
#Display1Exp:import#

# <exp>:Display1Exp ::= DISPLAY1 <exp>
class Display1Exp(Exp):

    __className = "Display1Exp"
    __ruleString =
        "<exp>:Display1Exp ::= DISPLAY1 <exp>"
    exp = None

    def __init__(self, exp):
        #Display1Exp:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:Display1Exp", scn.lno)
                scn$.match(Token.Match.DISPLAY1, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new Display1Exp(exp);

    #Display1Exp#
        