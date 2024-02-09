#SimpleLoc:top#
#SimpleLoc:import#

# <loc>:SimpleLoc ::= 
class SimpleLoc(Loc):

    __className = "SimpleLoc"
    __ruleString =
        "<loc>:SimpleLoc ::= "
    

    def __init__(self, ):
        #SimpleLoc:init#
        

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<loc>:SimpleLoc", scn.lno)
                return new SimpleLoc();

    #SimpleLoc#
        