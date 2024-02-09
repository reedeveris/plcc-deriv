#Mangle:top#
#Mangle:import#

# <mangle> **= RANGLE <exp> LPAREN <rands> RPAREN
class Mangle(None):

    __className = "Mangle"
    __ruleString =
        "<mangle> **= RANGLE <exp> LPAREN <rands> RPAREN"
    expList = None
		randsList = None

    def __init__(self, expList, randsList):
        #Mangle:init#
        self.expList = expList
			self.randsList = randsList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<mangle>", scn.lno)
        List<Exp> expList = new ArrayList<Exp>();
		List<Rands> randsList = new ArrayList<Rands>();
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
        case RANGLE:
            scn$.match(Token.Match.RANGLE, trace$);
			expList.add(Exp.parse(scn$, trace$));
			scn$.match(Token.Match.LPAREN, trace$);
			randsList.add(Rands.parse(scn$, trace$));
			scn$.match(Token.Match.RPAREN, trace$);
            continue
        default:
            return new Mangle(expList, randsList);

            

    #Mangle#
        