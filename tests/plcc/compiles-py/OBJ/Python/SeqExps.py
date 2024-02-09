#SeqExps:top#
#SeqExps:import#

# <seqExps> **= SEMI <exp>
class SeqExps(None):

    __className = "SeqExps"
    __ruleString =
        "<seqExps> **= SEMI <exp>"
    expList = None

    def __init__(self, expList):
        #SeqExps:init#
        self.expList = expList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<seqExps>", scn.lno)
        List<Exp> expList = new ArrayList<Exp>();
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
        case SEMI:
            scn$.match(Token.Match.SEMI, trace$);
			expList.add(Exp.parse(scn$, trace$));
            continue
        default:
            return new SeqExps(expList);

            

    #SeqExps#
        