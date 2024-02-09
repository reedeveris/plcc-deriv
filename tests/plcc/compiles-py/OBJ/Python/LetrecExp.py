#LetrecExp:top#
#LetrecExp:import#

# <exp>:LetrecExp ::= LETREC <letrecDecls> IN <exp>
class LetrecExp(Exp):

    __className = "LetrecExp"
    __ruleString =
        "<exp>:LetrecExp ::= LETREC <letrecDecls> IN <exp>"
    letrecDecls = None
		exp = None

    def __init__(self, letrecDecls, exp):
        #LetrecExp:init#
        self.letrecDecls = letrecDecls
			self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:LetrecExp", scn.lno)
                scn$.match(Token.Match.LETREC, trace$);
        LetrecDecls letrecDecls = LetrecDecls.parse(scn$, trace$);
        scn$.match(Token.Match.IN, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new LetrecExp(letrecDecls, exp);

    #LetrecExp#
        