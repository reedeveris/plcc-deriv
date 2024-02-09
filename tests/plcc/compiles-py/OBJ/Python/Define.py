#Define:top#
#Define:import#

# <program>:Define ::= DEFINE <VAR> EQUALS <exp>
class Define(Program):

    __className = "Define"
    __ruleString =
        "<program>:Define ::= DEFINE <VAR> EQUALS <exp>"
    var = None
		exp = None

    def __init__(self, var, exp):
        #Define:init#
        self.var = var
			self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<program>:Define", scn.lno)
                scn$.match(Token.Match.DEFINE, trace$);
        Token var = scn$.match(Token.Match.VAR, trace$);
        scn$.match(Token.Match.EQUALS, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new Define(var, exp);

    #Define#
        