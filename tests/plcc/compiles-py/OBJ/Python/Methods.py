#Methods:top#
#Methods:import#

# <methods> **= METHOD <VAR> EQUALS <proc>
class Methods(None):

    __className = "Methods"
    __ruleString =
        "<methods> **= METHOD <VAR> EQUALS <proc>"
    varList = None
		procList = None

    def __init__(self, varList, procList):
        #Methods:init#
        self.varList = varList
			self.procList = procList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<methods>", scn.lno)
        List<Token> varList = new ArrayList<Token>();
		List<Proc> procList = new ArrayList<Proc>();
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
        case METHOD:
            scn$.match(Token.Match.METHOD, trace$);
			varList.add(scn$.match(Token.Match.VAR, trace$));
			scn$.match(Token.Match.EQUALS, trace$);
			procList.add(Proc.parse(scn$, trace$));
            continue
        default:
            return new Methods(varList, procList);

            

    #Methods#
        