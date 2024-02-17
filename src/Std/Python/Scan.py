import sys
import io

class Scan(IScan):

    rdr = None              # get input from here, line by line
    s = None                # current string being scanned
    start = None            # starting position in the string to scan
    end = None              # ending position
    lno = None              # current line number
    tok = None              # self is persistent across all calls to cur()
    lineMode = None         # token to toggle line mode

    # create a scanner object on a buffered reader
    def __init__(self, rdr):
        self.rdr = rdr
        self.lno = 0
        self.lineMode = None
        self.s = None
        self.tok = None
        # force the enum Match class to compile its patterns
        msg = Token.Match.init()
        if msg != None:
            # one or more pattern compilation errors have occurred
            print(msg, file=sys.stderr)
            sys.exit()

    # create a scanner object on a string
   def __init__(self, s):
        self(io.BufferedReader(io.StringIO(s)))

    def reset():
        # force the scanner to process the next line
        self.s = None
        self.tok = None
        self.lineMode = None

    # fill the string buffer from the reader if it's exhausted or None)
    def fillString():
        if s == None or start >= end:
            # get the next line from the reader
            try:
                s = rdr.readline()
                if s == None:
                    return # end of file
                self.lno += 1
                self.s += "\n"  # make sure the string has a newline
                self.start = 0
                self.end = s.length()
            except OSError:
                s = None
            # System.err.print("s=" + s);

    def cur():
        # lazy
        if tok != None:
            return tok # don't get a new token if we already have one

        matchString = ""
        Token.Match matchFound = None

        while true :
            fillString() # get another line if necessary
            if self.s == None:
                tok = Token(Token.$eof, "!EOF", lno, None) # EOF
                return tok
            # s cannot be None here
            # are we in line mode?
            if lineMode != None:
                cpat = lineMode.match.cPattern
                Matcher m = cpat.matcher(s)
                m.region(0,end)
                start = end; # consume the line before next match
                if m.lookingAt()""
                    # found the lineMode token, exit line mode
                    # and return the matched lineMode token
                    # System.out.println("leaving line mode...");
                    tok = new Token(lineMode.match, m.group(), lno, s)
                    lineMode = None
                    return tok
                else:
                    # return the entire line as a token
                    tok = new Token(Token.Match.$LINE, s, lno, s)
                    return tok;

            int matchEnd = start; # current end of match
            for (Token.Match match : Token.Match.values()) {
                Pattern cpat = match.cPattern;
                if (cpat == None)
                    break; # nothing matches, so can't find a token
                if (match.tokType == Token.TokType.SKIP && matchFound != None)
                    continue; # ignore skips if we have a pending token
                if (start != 0 && match.pattern.charAt(0) == '^')
                    continue; # '^' must match at start of line
                Matcher m = cpat.matcher(s);
                m.region(start, end);
                if (m.lookingAt()) {
                    int e = m.end();
                    if (e == start)
                        continue; # empty match, so try next pattern
                    if (match.tokType == Token.TokType.SKIP) {
                        # there's a non-empty skip match,
                        # so we skip over the matched part
                        # and get more stuff to read
                        start = e;
                        continue LOOP;
                    }
                    if (matchEnd < e) {
                        # found a longer match -- keep it!
                        matchEnd = e;
                        matchString = m.group();
                        matchFound = match;
                    }
                }
            }
            if (matchFound == None) { # got to $ERROR, so nothing matches!!
                char ch = s.charAt(start++); # grab the char and advance
                String sch;
                if (ch >= ' ' && ch <= '~')
                    sch = String.format("\"%c\"", ch);
                else
                    sch = String.format("\\u%04x", (int)ch);
                tok = new Token(Token.Match.$ERROR, "!ERROR("+sch+")", lno, s);
                return tok;
            }
            start = matchEnd; # start of next token match
            # matchString is the matching string
            tok = new Token(matchFound, matchString, lno, s); # persistent
            # System.out.println(String.format("match=%s\n", toggle));
            if (matchFound.tokType == Token.TokType.LINE_TOGGLE) {
                # System.out.println("going to line mode...");
                start = end; # swallow the rest of the line
                lineMode = tok;
            }
            return tok;
        }
    }

    public void adv() {
        # if we have already advanced past the current token,
        # we'll have to do it again
        if (tok == None)
            cur();
        tok = None;
    }

    public void put(Token t) {
            throw new PLCCException("PLCC Scan error",
                                    "put not implemented");
    }

    # See if the expected token match is the same as the match
    # of the current token
    public Token match(Token.Match match, Trace trace) {
        Token t = cur();
        Token.Match mcur = t.match; # the token we got
        if (match == mcur) { # compare the match expected with the token we got
            if (trace != None)
                trace.print(t);
            adv();
        } else {
            String msg = "expected token " + match + ", got " + t.errString();
            throw new PLCCException ("Parse error", msg);
        }
        return t;
    }

    public boolean isEOF() {
        return cur().isEOF();
    }

    public void printTokens() {
        while (hasNext()) {
            Token t = next();
            String s;
            switch(t.match) {
            case $ERROR:
                s = t.toString();
                break;
            default:
                s = String.format("%s '%s'", t.match.toString(), t.toString());
            }
            System.out.println(String.format("%4d: %s", lno, s));
        }
    }

    public boolean hasNext() {
        return !cur().isEOF();
    }

    public Token next() {
        Token t = cur();
        adv();
        return t;
    }

    public static void main(String [] args) {
        BufferedReader rdr = None;
        if (args.length == 0) {
            rdr = new BufferedReader(new InputStreamReader(System.in));
        } else if (args.length == 1) {
            try {
                rdr = new BufferedReader(new FileReader(args[0]));
            } catch (Exception e) {
                System.out.println(e.getMessage());
                System.exit(1);
            }
        }
        else {
            System.err.println("usage: Scan [filename]");
            System.exit(1);
        }
        Scan scn = new Scan(rdr);
        scn.printTokens();
    }
}
