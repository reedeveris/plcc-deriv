#AppExp:top#
#AppExp:import#

# <exp>:AppExp ::= DOT <exp> LPAREN <rands> RPAREN
class AppExp(Exp):

    __className = "AppExp"
    __ruleString =
        "<exp>:AppExp ::= DOT <exp> LPAREN <rands> RPAREN"
    exp = None
		rands = None

    def __init__(self, exp, rands):
        #AppExp:init#
        self.exp = exp
			self.rands = rands

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:AppExp", scn.lno)
                scn$.match(Token.Match.DOT, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        scn$.match(Token.Match.LPAREN, trace$);
        Rands rands = Rands.parse(scn$, trace$);
        scn$.match(Token.Match.RPAREN, trace$);
        return new AppExp(exp, rands);

    #AppExp#
        