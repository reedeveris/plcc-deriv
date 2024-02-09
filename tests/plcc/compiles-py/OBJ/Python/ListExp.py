#ListExp:top#
#ListExp:import#

# <exp>:ListExp ::= LBRACK <rands> RBRACK
class ListExp(Exp):

    __className = "ListExp"
    __ruleString =
        "<exp>:ListExp ::= LBRACK <rands> RBRACK"
    rands = None

    def __init__(self, rands):
        #ListExp:init#
        self.rands = rands

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:ListExp", scn.lno)
                scn$.match(Token.Match.LBRACK, trace$);
        Rands rands = Rands.parse(scn$, trace$);
        scn$.match(Token.Match.RBRACK, trace$);
        return new ListExp(rands);

    #ListExp#
        