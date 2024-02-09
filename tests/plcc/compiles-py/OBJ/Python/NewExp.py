#NewExp:top#
#NewExp:import#

# <exp>:NewExp ::= NEW <exp>
class NewExp(Exp):

    __className = "NewExp"
    __ruleString =
        "<exp>:NewExp ::= NEW <exp>"
    exp = None

    def __init__(self, exp):
        #NewExp:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:NewExp", scn.lno)
                scn$.match(Token.Match.NEW, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new NewExp(exp);

    #NewExp#
        