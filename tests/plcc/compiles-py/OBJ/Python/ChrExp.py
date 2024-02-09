#ChrExp:top#
#ChrExp:import#

# <exp>:ChrExp ::= <CHR>
class ChrExp(Exp):

    __className = "ChrExp"
    __ruleString =
        "<exp>:ChrExp ::= <CHR>"
    chr = None

    def __init__(self, chr):
        #ChrExp:init#
        self.chr = chr

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:ChrExp", scn.lno)
                Token chr = scn$.match(Token.Match.CHR, trace$);
        return new ChrExp(chr);

    #ChrExp#
        