#ClassExp:top#
#ClassExp:import#

# <exp>:ClassExp ::= <classDecl>
class ClassExp(Exp):

    __className = "ClassExp"
    __ruleString =
        "<exp>:ClassExp ::= <classDecl>"
    classDecl = None

    def __init__(self, classDecl):
        #ClassExp:init#
        self.classDecl = classDecl

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<exp>:ClassExp", scn.lno)
                ClassDecl classDecl = ClassDecl.parse(scn$, trace$);
        return new ClassExp(classDecl);

    #ClassExp#
        