#LetExp:top#
#LetExp:import#

# <exp>:LetExp ::= LET <letDecls> IN <exp>
class LetExp(Exp):

    __className = "LetExp"
    __ruleString =
        "<exp>:LetExp ::= LET <letDecls> IN <exp>"
    letDecls = None
		exp = None

    def __init__(self, letDecls, exp):
        #LetExp:init#
        self.letDecls = letDecls
			self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:LetExp", scn.lno)
                scn$.match(Token.Match.LET, trace$);
        LetDecls letDecls = LetDecls.parse(scn$, trace$);
        scn$.match(Token.Match.IN, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new LetExp(letDecls, exp);

    #LetExp#
        