from plcc import defangRHS

class Formatter():

    def __init__(self):
        pass
    
    def toString(self):
        return "No language specified."

    def formatAbstractStub(self,base,cases,nt2cls):
        pass
    def formatStub(self,extends,cls,lhs,fieldVars,ruleString,parseString,nt2cls):
        pass
    def formatArbnoParse(self, cls, rhs, sep, inits, args, loopList, fieldVars, fieldSet, rhsString, switchCases):
        pass
    def formatInjection(self, stub, cls, mod, codeString, num):
        pass



##########################
######### PYTHON #########
##########################

class PythonFormatter(Formatter):

    def __init__(self):
        pass
    
    def toString(self):
        return "Python"

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
                cases='\n\t\t\t'.join(caseList)
                )
        return stubString
    
    def formatStub(self,extends,cls,lhs,fieldVars,ruleString,parseString,nt2cls):
        ext = None
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
                decls='\n\t\t'.join(decls),
                params=', '.join(params),
                inits='\n\t\t\t'.join(inits),
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

            """.format(inits='\n\t\t'.join(inits),
            switchCases='\n\t\t'.join(switchCases),
            loopList='\n\t\t\t'.join(loopList),
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
            """.format(inits='\n\t\t'.join(inits),
            switchCases='\n\t\t'.join(switchCases),
            loopList='\n\t\t\t\t'.join(loopList),
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




##########################
########## JAVA ##########
##########################

class JavaFormatter(Formatter):

    def __init__(self):
        pass
    
    def toString(self):
        return "Java"

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
                cases='\n\t\t\t'.join(caseList)
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
                decls='\n\t'.join(decls),
                params=', '.join(params),
                inits='\n\t\t'.join(inits),
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
        """.format(inits='\n\t\t'.join(inits),
            switchCases='\n\t\t'.join(switchCases),
            loopList='\n\t\t\t'.join(loopList),
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
            """.format(inits='\n\t\t'.join(inits),
            switchCases='\n\t\t'.join(switchCases),
            loopList='\n\t\t\t\t'.join(loopList),
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