#EenvExp:top#
#EenvExp:import#

# <exp>:EenvExp ::= LLANGLE <exp> <mangle> RRANGLE
class EenvExp(Exp):

    __className = "EenvExp"
    __ruleString =
        "<exp>:EenvExp ::= LLANGLE <exp> <mangle> RRANGLE"
    exp = None
		mangle = None

    def __init__(self, exp, mangle):
        #EenvExp:init#
        self.exp = exp
			self.mangle = mangle

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:EenvExp", scn.lno)
                scn$.match(Token.Match.LLANGLE, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        Mangle mangle = Mangle.parse(scn$, trace$);
        scn$.match(Token.Match.RRANGLE, trace$);
        return new EenvExp(exp, mangle);

    #EenvExp#
        