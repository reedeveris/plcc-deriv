#ClassDecl:top#
#ClassDecl:import#

# <classDecl> ::= CLASS <ext> <statics> <fields> <methods> END
class ClassDecl(None):

    __className = "ClassDecl"
    __ruleString =
        "<classDecl> ::= CLASS <ext> <statics> <fields> <methods> END"
    ext = None
		statics = None
		fields = None
		methods = None

    def __init__(self, ext, statics, fields, methods):
        #ClassDecl:init#
        self.ext = ext
			self.statics = statics
			self.fields = fields
			self.methods = methods

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("<classDecl>", scn.lno)
                scn$.match(Token.Match.CLASS, trace$);
        Ext ext = Ext.parse(scn$, trace$);
        Statics statics = Statics.parse(scn$, trace$);
        Fields fields = Fields.parse(scn$, trace$);
        Methods methods = Methods.parse(scn$, trace$);
        scn$.match(Token.Match.END, trace$);
        return new ClassDecl(ext, statics, fields, methods);

    #ClassDecl#
        