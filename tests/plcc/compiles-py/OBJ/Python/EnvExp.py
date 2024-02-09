#EnvExp:top#
#EnvExp:import#

# <exp>:EnvExp ::= LANGLE <exp>vExp RANGLE <exp>eExp
class EnvExp(Exp):

    __className = "EnvExp"
    __ruleString =
        "<exp>:EnvExp ::= LANGLE <exp>vExp RANGLE <exp>eExp"
    vExp = None
		eExp = None

    def __init__(self, vExp, eExp):
        #EnvExp:init#
        self.vExp = vExp
			self.eExp = eExp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:EnvExp", scn.lno)
                scn$.match(Token.Match.LANGLE, trace$);
        Exp vExp = Exp.parse(scn$, trace$);
        scn$.match(Token.Match.RANGLE, trace$);
        Exp eExp = Exp.parse(scn$, trace$);
        return new EnvExp(vExp, eExp);

    #EnvExp#
        