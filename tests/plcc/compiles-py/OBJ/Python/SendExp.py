#SendExp:top#
#SendExp:import#

# <exp>:SendExp ::= SEND <exp>objExp <exp>procExp LPAREN <rands> RPAREN
class SendExp(Exp):

    __className = "SendExp"
    __ruleString =
        "<exp>:SendExp ::= SEND <exp>objExp <exp>procExp LPAREN <rands> RPAREN"
    objExp = None
		procExp = None
		rands = None

    def __init__(self, objExp, procExp, rands):
        #SendExp:init#
        self.objExp = objExp
			self.procExp = procExp
			self.rands = rands

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:SendExp", scn.lno)
                scn$.match(Token.Match.SEND, trace$);
        Exp objExp = Exp.parse(scn$, trace$);
        Exp procExp = Exp.parse(scn$, trace$);
        scn$.match(Token.Match.LPAREN, trace$);
        Rands rands = Rands.parse(scn$, trace$);
        scn$.match(Token.Match.RPAREN, trace$);
        return new SendExp(objExp, procExp, rands);

    #SendExp#
        