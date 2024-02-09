#LetDecls:top#
#LetDecls:import#

# <letDecls> **= <VAR> EQUALS <exp>
class LetDecls(None):

    __className = "LetDecls"
    __ruleString =
        "<letDecls> **= <VAR> EQUALS <exp>"
    varList = None
		expList = None

    def __init__(self, varList, expList):
        #LetDecls:init#
        self.varList = varList
			self.expList = expList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<letDecls>", scn.lno)
        List<Token> varList = new ArrayList<Token>();
		List<Exp> expList = new ArrayList<Exp>();
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
        case VAR:
            varList.add(scn$.match(Token.Match.VAR, trace$));
			scn$.match(Token.Match.EQUALS, trace$);
			expList.add(Exp.parse(scn$, trace$));
            continue
        default:
            return new LetDecls(varList, expList);

            

    #LetDecls#
        