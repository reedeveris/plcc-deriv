#Rands:top#
#Rands:import#

# <rands> **= <exp> +COMMA
class Rands(None):

    __className = "Rands"
    __ruleString =
        "<rands> **= <exp> +COMMA"
    expList = None

    def __init__(self, expList):
        #Rands:init#
        self.expList = expList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<rands>", scn.lno)
        List<Exp> expList = new ArrayList<Exp>();
# first trip through the parse
t = scn.cur()
Token.Match match = t.match
    match match:
        case LIT:
		case MULOP:
		case AT:
		case LET:
		case LBRACE:
		case GTP:
		case ZEROP:
		case ADD1OP:
		case OBJECTP:
		case CHR:
		case LETREC:
		case PUTC:
		case DISPLAY1:
		case LENOP:
		case VAR:
		case LANGLE:
		case ERROR:
		case PROC:
		case BANGAT:
		case ATAT:
		case DISPLAY:
		case SET:
		case GEP:
		case DIVOP:
		case LBRACK:
		case LLANGLE:
		case EQP:
		case CLASS:
		case NEP:
		case NEW:
		case PERROR:
		case ADDFIRSTOP:
		case NEWLINE:
		case DOT:
		case SEND:
		case WITH:
		case SUBOP:
		case FIRSTOP:
		case SUB1OP:
		case STRNG:
		case NIL:
		case CLASSP:
		case LISTP:
		case ADDOP:
		case IF:
		case LTP:
		case EXIT:
		case RESTOP:
		case LEP:
            while(true) {
                expList.add(Exp.parse(scn$, trace$));
                t = scn.cur()
                match = t.match
                if match != Token.Match.COMMA:
                    break # not a separator, so we're done
                scn.match(match, trace)
        # end of switch
    return new Rands(expList);
            

    #Rands#
        