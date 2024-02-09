#Proc:top#
#Proc:import#

# <proc> ::= PROC LPAREN <formals> RPAREN <exp>
class Proc(None):

    __className = "Proc"
    __ruleString =
        "<proc> ::= PROC LPAREN <formals> RPAREN <exp>"
    formals = None
		exp = None

    def __init__(self, formals, exp):
        #Proc:init#
        self.formals = formals
			self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<proc>", scn.lno)
                scn$.match(Token.Match.PROC, trace$);
        scn$.match(Token.Match.LPAREN, trace$);
        Formals formals = Formals.parse(scn$, trace$);
        scn$.match(Token.Match.RPAREN, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new Proc(formals, exp);

    #Proc#
        