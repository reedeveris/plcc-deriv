#Ext1:top#
#Ext1:import#

# <ext>:Ext1 ::= EXTENDS <exp>
class Ext1(Ext):

    __className = "Ext1"
    __ruleString =
        "<ext>:Ext1 ::= EXTENDS <exp>"
    exp = None

    def __init__(self, exp):
        #Ext1:init#
        self.exp = exp

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<ext>:Ext1", scn.lno)
                scn$.match(Token.Match.EXTENDS, trace$);
        Exp exp = Exp.parse(scn$, trace$);
        return new Ext1(exp);

    #Ext1#
        