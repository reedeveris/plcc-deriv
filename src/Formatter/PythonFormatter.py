from .Formatter import Formatter

class PythonFormatter(Formatter):

    def __init__(self):
        pass

    def toString(self):
        return "Python"

    def indent(self, n, iList):
        ### make a new list with the old list items prepended with 4*n spaces
        indentString = '\t'*n
        newList = []
        for item in iList:
            newList.append('{}{}'.format(indentString, item))
        # print('### str={}'.format(str))
        return newList

    def formatAbstractStub(self,base,cases,caseList,nt2cls):
        if base == nt2cls:
            ext = '_Start'
        else:
            ext = ''
        stubString = """\
#{base}:top#
#{base}:import#

class {base}({ext}, ABC) :

    __className = "{base}"

    def parse(scn, trace):
        t = scn.cur()
        Token.Match match = t.match
        match match:
{cases}
            case _:
                raise PLCCException(
                    "Parse error",
                    "{base} cannot begin with " + t$.errString()
                )

    #{base}#
        """.format(base=base,
                ext=ext,
                cases='\n'.join(self.indent(3,caseList))
                )
        return stubString

    def formatStub(self,extends,cls,lhs,fieldVars,ruleString,parseString,nt2cls):
        ext = ''
        if cls in extends:
            ext = extends[cls]
        else:
            pass
        # fieldVars = makeVars(cls, rhs)
        decls = []
        inits = []
        params = []
        for (field, fieldType) in fieldVars:
            decls.append('{} = None'.format(field))
            inits.append('self.{} = {}'.format(field, field))
            params.append('{}'.format(field))
        if cls == nt2cls:
            ext = '_Start'
        stubString = """\
#{cls}:top#
#{cls}:import#

# {ruleString}
class {cls}({ext}):

    __className = "{cls}"
    __ruleString =
        "{ruleString}"
{decls}

    def __init__(self, {params}):
        #{cls}:init#
{inits}

    def parse(scn, trace):
        if trace not null:
            trace = trace.nonterm("{lhs}", scn.lno)
        {parse}

    #{cls}#
        """.format(cls=cls,
                lhs=lhs,
                ext=ext,
                ruleString=ruleString,
                decls='\n'.join(self.indent(1,decls)),
                params=', '.join(params),
                inits='\n'.join(self.indent(2,inits)),
                parse=parseString)
        return stubString

    def formatArbnoParse(self, cls, rhs, sep, inits, args, loopList, fieldVars, fieldSet, rhsString, switchCases, returnItem):
        if sep == None:
            # no separator
            parseString = """\
{inits}
while true:
    t = scn.cur()
    Token.Match match = t.match
    match match:
{switchCases}
{loopList}
            continue
        default:
            {returnItem}

            """.format(inits='\n'.join(self.indent(2,inits)),
            switchCases='\n'.join(self.indent(2,switchCases)),
            loopList='\n'.join(self.indent(3,loopList)),
            returnItem=returnItem)
        else:
            # there's a separator
            parseString = """\
{inits}
# first trip through the parse
t = scn.cur()
Token.Match match = t.match
    match match:
{switchCases}
            while(true) {{
{loopList}
                t = scn.cur()
                match = t.match
                if match != Token.Match.{sep}:
                    break # not a separator, so we're done
                scn.match(match, trace)
        # end of switch
    {returnItem}
            """.format(inits='\n'.join(self.indent(2,inits)),
            switchCases='\n'.join(self.indent(2,switchCases)),
            loopList='\n'.join(self.indent(4,loopList)),
            returnItem=returnItem,
            sep=sep)
        return (fieldVars, parseString)

    def formatInjection(self, stub, cls, mod, codeString, num):
        if num == 1:
            repl = '#{}:{}#'.format(cls, mod)
            stub = stub.replace(repl, '{}\n{}'.format(codeString,repl))
            repl = '#{}:{}#'.format(cls, mod)
            stub = stub.replace(repl, '{} {}'.format(codeString,repl))
        else:
            repl = '//{}//'.format(cls)
            stub = stub.replace(repl, '{}\n\n{}'.format(codeString,repl))
        return stub
