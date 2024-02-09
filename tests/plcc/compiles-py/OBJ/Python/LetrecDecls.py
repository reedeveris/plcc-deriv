#LetrecDecls:top#
#LetrecDecls:import#

# <letrecDecls> **= <VAR> EQUALS <proc>
class LetrecDecls(None):

    __className = "LetrecDecls"
    __ruleString =
        "<letrecDecls> **= <VAR> EQUALS <proc>"
    varList = None
		procList = None

    def __init__(self, varList, procList):
        #LetrecDecls:init#
        self.varList = varList
			self.procList = procList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<letrecDecls>", scn.lno)
        List<Token> varList = new ArrayList<Token>();
		List<Proc> procList = new ArrayList<Proc>();
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
        case VAR:
            varList.add(scn$.match(Token.Match.VAR, trace$));
			scn$.match(Token.Match.EQUALS, trace$);
			procList.add(Proc.parse(scn$, trace$));
            continue
        default:
            return new LetrecDecls(varList, procList);

            

    #LetrecDecls#
        