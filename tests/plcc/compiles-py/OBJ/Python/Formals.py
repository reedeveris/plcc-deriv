#Formals:top#
#Formals:import#

# <formals> **= <VAR> +COMMA
class Formals(None):

    __className = "Formals"
    __ruleString =
        "<formals> **= <VAR> +COMMA"
    varList = None

    def __init__(self, varList):
        #Formals:init#
        self.varList = varList

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<formals>", scn.lno)
        List<Token> varList = new ArrayList<Token>();
# first trip through the parse
t = scn.cur()
Token.Match match = t.match
    match match:
        case VAR:
            while(true) {
                varList.add(scn$.match(Token.Match.VAR, trace$));
                t = scn.cur()
                match = t.match
                if match != Token.Match.COMMA:
                    break # not a separator, so we're done
                scn.match(match, trace)
        # end of switch
    return new Formals(varList);
            

    #Formals#
        