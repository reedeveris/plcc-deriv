#Program:top#
#Program:import#

class Program(_Start, ABC) :

    __className = "Program"

    def parse(scn, trace):
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
				return Eval.parse(scn$,trace$);
			case DEFINE:
				return Define.parse(scn$,trace$);
            case _:
                raise PLCCException(
                    "Parse error",
                    "Program cannot begin with " + t$.errString()
                )

    #Program#
        