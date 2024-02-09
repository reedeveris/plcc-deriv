#Fields:top#
#Fields:import#

# <fields> **= FIELD <VAR>
class Fields(None):

    __className = "Fields"
    __ruleString =
        "<fields> **= FIELD <VAR>"
    varList = None

    def __init__(self, varList):
        #Fields:init#
        self.varList = varList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<fields>", scn.lno)
        List<Token> varList = new ArrayList<Token>();
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
        case FIELD:
            scn$.match(Token.Match.FIELD, trace$);
			varList.add(scn$.match(Token.Match.VAR, trace$));
            continue
        default:
            return new Fields(varList);

            

    #Fields#
        