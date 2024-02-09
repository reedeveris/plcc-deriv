#ObjLoc:top#
#ObjLoc:import#

# <loc>:ObjLoc ::= LANGLE <exp> RANGLE
class ObjLoc(Loc):

    __className = "ObjLoc"
    __ruleString =
        "<loc>:ObjLoc ::= LANGLE <exp> RANGLE"
    exp = None

    def __init__(self, exp):
        #ObjLoc:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<loc>:ObjLoc", scn.lno)
                scn$.match(Token.Match.LANGLE, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        scn$.match(Token.Match.RANGLE, trace$);
        return new ObjLoc(exp);

    #ObjLoc#
        