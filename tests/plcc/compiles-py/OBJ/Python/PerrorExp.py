#PerrorExp:top#
#PerrorExp:import#

# <exp>:PerrorExp ::= PERROR <STRNG>
class PerrorExp(Exp):

    __className = "PerrorExp"
    __ruleString =
        "<exp>:PerrorExp ::= PERROR <STRNG>"
    strng = None

    def __init__(self, strng):
        #PerrorExp:init#
        self.strng = strng

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:PerrorExp", scn.lno)
                scn$.match(Token.Match.PERROR, trace$);
        Token strng = scn$.match(Token.Match.STRNG, trace$);
        return new PerrorExp(strng);

    #PerrorExp#
        