#ClasspPrim:top#
#ClasspPrim:import#

# <prim>:ClasspPrim ::= CLASSP
class ClasspPrim(Prim):

    __className = "ClasspPrim"
    __ruleString =
        "<prim>:ClasspPrim ::= CLASSP"
    

    def __init__(self, ):
        #ClasspPrim:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<prim>:ClasspPrim", scn.lno)
                scn$.match(Token.Match.CLASSP, trace$);
        return new ClasspPrim();

    #ClasspPrim#
        