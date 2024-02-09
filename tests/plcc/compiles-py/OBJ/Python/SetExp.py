#SetExp:top#
#SetExp:import#

# <exp>:SetExp ::= SET <loc> <VAR> EQUALS <exp>
class SetExp(Exp):

    __className = "SetExp"
    __ruleString =
        "<exp>:SetExp ::= SET <loc> <VAR> EQUALS <exp>"
    loc = None
		var = None
		exp = None

    def __init__(self, loc, var, exp):
        #SetExp:init#
        self.loc = loc
			self.var = var
			self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:SetExp", scn.lno)
                scn$.match(Token.Match.SET, trace$);
        Loc loc = Loc.parse(scn$, trace$);
        Token var = scn$.match(Token.Match.VAR, trace$);
        scn$.match(Token.Match.EQUALS, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new SetExp(loc, var, exp);

    #SetExp#
        