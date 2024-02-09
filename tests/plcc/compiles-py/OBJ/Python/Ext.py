#Ext:top#
#Ext:import#

class Ext(, ABC) :

    __className = "Ext"

    def parse(scn, trace):
        t = scn.cur()
        Token.Match match = t.match
        match match:
            case EXTENDS:
				return Ext1.parse(scn$,trace$);
			case STATIC:
			case METHOD:
			case FIELD:
			case END:
				return Ext0.parse(scn$,trace$);
            case _:
                raise PLCCException(
                    "Parse error",
                    "Ext cannot begin with " + t$.errString()
                )

    #Ext#
        