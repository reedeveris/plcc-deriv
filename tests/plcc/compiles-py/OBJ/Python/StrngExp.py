#StrngExp:top#
#StrngExp:import#

# <exp>:StrngExp ::= <STRNG>
class StrngExp(Exp):

    __className = "StrngExp"
    __ruleString =
        "<exp>:StrngExp ::= <STRNG>"
    strng = None

    def __init__(self, strng):
        #StrngExp:init#
        self.strng = strng

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:StrngExp", scn.lno)
                Token strng = scn$.match(Token.Match.STRNG, trace$);
        return new StrngExp(strng);

    #StrngExp#
        