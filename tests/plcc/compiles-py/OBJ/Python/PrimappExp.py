#PrimappExp:top#
#PrimappExp:import#

# <exp>:PrimappExp ::= <prim> LPAREN <rands> RPAREN
class PrimappExp(Exp):

    __className = "PrimappExp"
    __ruleString =
        "<exp>:PrimappExp ::= <prim> LPAREN <rands> RPAREN"
    prim = None
		rands = None

    def __init__(self, prim, rands):
        #PrimappExp:init#
        self.prim = prim
			self.rands = rands

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:PrimappExp", scn.lno)
                Prim prim = Prim.parse(scn$, trace$);
        scn$.match(Token.Match.LPAREN, trace$);
        Rands rands = Rands.parse(scn$, trace$);
        scn$.match(Token.Match.RPAREN, trace$);
        return new PrimappExp(prim, rands);

    #PrimappExp#
        