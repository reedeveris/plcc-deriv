#Statics:top#
#Statics:import#

# <statics> **= STATIC <VAR> EQUALS <exp>
class Statics(None):

    __className = "Statics"
    __ruleString =
        "<statics> **= STATIC <VAR> EQUALS <exp>"
    varList = None
		expList = None

    def __init__(self, varList, expList):
        #Statics:init#
        self.varList = varList
			self.expList = expList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<statics>", scn.lno)
        List<Token> varList = new ArrayList<Token>();
		List<Exp> expList = new ArrayList<Exp>();
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
        case STATIC:
            scn$.match(Token.Match.STATIC, trace$);
			varList.add(scn$.match(Token.Match.VAR, trace$));
			scn$.match(Token.Match.EQUALS, trace$);
			expList.add(Exp.parse(scn$, trace$));
            continue
        default:
            return new Statics(varList, expList);

            

    #Statics#
        