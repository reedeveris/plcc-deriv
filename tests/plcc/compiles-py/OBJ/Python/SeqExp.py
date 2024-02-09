#SeqExp:top#
#SeqExp:import#

# <exp>:SeqExp ::= LBRACE <exp> <seqExps> RBRACE
class SeqExp(Exp):

    __className = "SeqExp"
    __ruleString =
        "<exp>:SeqExp ::= LBRACE <exp> <seqExps> RBRACE"
    exp = None
		seqExps = None

    def __init__(self, exp, seqExps):
        #SeqExp:init#
        self.exp = exp
			self.seqExps = seqExps

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:SeqExp", scn.lno)
                scn$.match(Token.Match.LBRACE, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        SeqExps seqExps = SeqExps.parse(scn$, trace$);
        scn$.match(Token.Match.RBRACE, trace$);
        return new SeqExp(exp, seqExps);

    #SeqExp#
        