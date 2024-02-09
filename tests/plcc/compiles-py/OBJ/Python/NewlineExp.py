#NewlineExp:top#
#NewlineExp:import#

# <exp>:NewlineExp ::= NEWLINE
class NewlineExp(Exp):

    __className = "NewlineExp"
    __ruleString =
        "<exp>:NewlineExp ::= NEWLINE"
    

    def __init__(self, ):
        #NewlineExp:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:NewlineExp", scn.lno)
                scn$.match(Token.Match.NEWLINE, trace$);
        return new NewlineExp();

    #NewlineExp#
        