#WithExp:top#
#WithExp:import#

# <exp>:WithExp ::= WITH <exp>vExp EVAL <exp>eExp
class WithExp(Exp):

    __className = "WithExp"
    __ruleString =
        "<exp>:WithExp ::= WITH <exp>vExp EVAL <exp>eExp"
    vExp = None
		eExp = None

    def __init__(self, vExp, eExp):
        #WithExp:init#
        self.vExp = vExp
			self.eExp = eExp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:WithExp", scn.lno)
                scn$.match(Token.Match.WITH, trace$);
        Exp vExp = Exp.parse(scn$, trace$);
        scn$.match(Token.Match.EVAL, trace$);
        Exp eExp = Exp.parse(scn$, trace$);
        return new WithExp(vExp, eExp);

    #WithExp#
        