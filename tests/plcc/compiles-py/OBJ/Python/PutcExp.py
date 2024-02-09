#PutcExp:top#
#PutcExp:import#

# <exp>:PutcExp ::= PUTC <exp>
class PutcExp(Exp):

    __className = "PutcExp"
    __ruleString =
        "<exp>:PutcExp ::= PUTC <exp>"
    exp = None

    def __init__(self, exp):
        #PutcExp:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:PutcExp", scn.lno)
                scn$.match(Token.Match.PUTC, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new PutcExp(exp);

    #PutcExp#
        