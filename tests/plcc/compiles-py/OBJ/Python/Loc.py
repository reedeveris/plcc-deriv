#Loc:top#
#Loc:import#

class Loc(, ABC) :

    __className = "Loc"

    def parse(scn, trace):
        t = scn.cur()
        Token.Match match = t.match
        match match:
            case LANGLE:
				return ObjLoc.parse(scn$,trace$);
			case VAR:
				return SimpleLoc.parse(scn$,trace$);
            case _:
                raise PLCCException(
                    "Parse error",
                    "Loc cannot begin with " + t$.errString()
                )

    #Loc#
        