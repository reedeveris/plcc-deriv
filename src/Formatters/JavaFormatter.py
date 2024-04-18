import Formatter

class JavaFormatter(Formatter):

    def __init__(self):
        pass
    
    def toString(self):
        return "Java"
    
    def indent(n, iList):
    ### make a new list with the old list items prepended with 4*n spaces
        indentString = '    '*n
        newList = []
        for item in iList:
            newList.append('{}{}'.format(indentString, item))
        # print('### str={}'.format(str))
        return newList

    def formatAbstractStub(self,base,cases,caseList,nt2cls):
        if base == nt2cls:
            ext = ' extends _Start'
        else:
            ext = ''
        stubString = """\
//{base}:top//
//{base}:import//
import java.util.*;

public abstract class {base}{ext} /*{base}:class*/ {{

    public static final String $className = "{base}";

    public static {base} parse(Scan scn$, Trace trace$) {{
        Token t$ = scn$.cur();
        Token.Match match$ = t$.match;
        switch(match$) {{
            {cases}
            default:
                throw new PLCCException(
                    "Parse error",
                    "{base} cannot begin with " + t$.errString()
                );
            }}
         }}

    //{base}//
}}
            """.format(base=base,
                ext=ext,
                cases='\n'.join(indent(3,caseList))
                )
        return stubString

    def formatStub(self,extends,cls,lhs,fieldVars,ruleString,parseString,nt2cls):
        ext = None
        if cls in extends:
            ext = ' extends {}'.format(extends[cls])
        else:
            pass
        # fieldVars = makeVars(cls, rhs)
        decls = []
        inits = []
        params = []
        for (field, fieldType) in fieldVars:
            decls.append('public {} {};'.format(fieldType, field))
            inits.append('this.{} = {};'.format(field, field))
            params.append('{} {}'.format(fieldType, field))
        if cls == nt2cls:
            ext = ' extends _Start'
        stubString = """\
//{cls}:top//
//{cls}:import//
import java.util.*;

// {ruleString}
public class {cls}{ext} /*{cls}:class*/ {{

    public static final String $className = "{cls}";
    public static final String $ruleString =
        "{ruleString}";
{decls}

    public {cls}({params}) {{
        //{cls}:init//
{inits}
    }}

    public static {cls} parse(Scan scn$, Trace trace$) {{
        if (trace$ != null)
            trace$ = trace$.nonterm("{lhs}", scn$.lno);
        {parse}
    }}

    //{cls}//
}}
            """.format(cls=cls,
                lhs=lhs,
                ext=ext,
                ruleString=ruleString,
                decls='\n'.join(indent(1,decls)),
                params=', '.join(params),
                inits='\n'.join(indent(2,inits)),
                parse=parseString)
        return stubString

    def formatArbnoParse(self, cls, rhs, sep, inits, args, loopList, fieldVars, fieldSet, rhsString, switchCases, returnItem):
        if sep == None:
            # no separator
            parseString = """\
{inits}
while (true) {{
    Token t$ = scn$.cur();
    Token.Match match$ = t$.match;
    switch(match$) {{
{switchCases}
{loopList}
            continue;
        default:
            {returnItem}
    }}
}}
        """.format(inits='\n'.join(indent(2,inits)),
            switchCases='\n'.join(indent(2,switchCases)),
            loopList='\n'.join(indent(3,loopList)),
            returnItem=returnItem)
        else:
            # there's a separator
            parseString = """\
{inits}
// first trip through the parse
Token t$ = scn$.cur();
Token.Match match$ = t$.match;
switch(match$) {{
{switchCases}
    while(true) {{
{loopList}
        t$ = scn$.cur();
        match$ = t$.match;
        if (match$ != Token.Match.{sep})
            break; // not a separator, so we're done
        scn$.match(match$, trace$);
    }}
}} // end of switch
{returnItem}
            """.format(inits='\n'.join(indent(2,inits)),
            switchCases='\n'.join(indent(2,switchCases)),
            loopList='\n'.join(indent(3,loopList)),
            returnItem=returnItem,
            sep=sep)
        return (fieldVars, parseString)
    
    def formatInjection(self, stub, cls, mod, codeString, num):
        if num == 1:
            repl = '//{}:{}//'.format(cls, mod)
            stub = stub.replace(repl, '{}\n{}'.format(codeString,repl))
            repl = '/*{}:{}*/'.format(cls, mod)
            stub = stub.replace(repl, '{} {}'.format(codeString,repl))
        else:
            repl = '//{}//'.format(cls)
            stub = stub.replace(repl, '{}\n\n{}'.format(codeString,repl))
        return stub