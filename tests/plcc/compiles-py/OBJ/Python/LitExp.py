#LitExp:top#
#LitExp:import#

# <exp>:LitExp ::= <LIT>
class LitExp(Exp):

    __className = "LitExp"
    __ruleString =
        "<exp>:LitExp ::= <LIT>"
    lit = None

    def __init__(self, lit):
        #LitExp:init#
        self.lit = lit

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:LitExp", scn.lno)
                Token lit = scn$.match(Token.Match.LIT, trace$);
        return new LitExp(lit);

    #LitExp#
        