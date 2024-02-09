#IfExp:top#
#IfExp:import#

# <exp>:IfExp ::= IF <exp>testExp THEN <exp>trueExp ELSE <exp>falseExp
class IfExp(Exp):

    __className = "IfExp"
    __ruleString =
        "<exp>:IfExp ::= IF <exp>testExp THEN <exp>trueExp ELSE <exp>falseExp"
    testExp = None
		trueExp = None
		falseExp = None

    def __init__(self, testExp, trueExp, falseExp):
        #IfExp:init#
        self.testExp = testExp
			self.trueExp = trueExp
			self.falseExp = falseExp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:IfExp", scn.lno)
                scn$.match(Token.Match.IF, trace$);
        Exp testExp = Exp.parse(scn$, trace$);
        scn$.match(Token.Match.THEN, trace$);
        Exp trueExp = Exp.parse(scn$, trace$);
        scn$.match(Token.Match.ELSE, trace$);
        Exp falseExp = Exp.parse(scn$, trace$);
        return new IfExp(testExp, trueExp, falseExp);

    #IfExp#
        