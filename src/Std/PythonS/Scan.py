import sys
import io
import re

class Scan(IScan):

    rdr = None              # get input from here, line by line
    s = None                # current string being scanned
    start = None            # starting position in the string to scan
    end = None              # ending position
    lno = None              # current line number
    tok = None              # self is persistent across all calls to cur()
    self.lineMode = None         # token to toggle line mode

    # create a scanner object on a buffered reader
    def __init__(self, rdr):
        self.rdr = rdr
        self.lno = 0
        self.self.lineMode = None
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
        self(io.BufferedReader(io.TextIO(s)))

    def reset(self):
        # force the scanner to process the next line
        self.s = None
        self.tok = None
        self.self.lineMode = None

    # fill the string buffer from the reader if it's exhausted or None)
    def fillString(self):
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

    def cur(self):
        # lazy
        if self.tok != None:
            return self.tok # don't get a new token if we already have one

        matchString = ""
        matchFound = None

        LOOP:
        while true :
            fillString() # get another line if necessary
            if self.s == None:
                self.tok = Token(Token.eof, "!EOF", lno, None) # EOF
                return self.tok
            # s cannot be None here
            # are we in line mode?
            if self.lineMode != None:
                cpat = self.lineMode.match.cPattern
                m = re.match(cpat, s)
                m.pos = 0
                m.endpos = end
                start = end # consume the line before next match
                if m:
                    # found the self.lineMode token, exit line mode
                    # and return the matched self.lineMode token
                    # System.out.println("leaving line mode...");
                    self.tok = Token(self.lineMode.match, m.group(), lno, s)
                    self.lineMode = None
                    return self.tok
                else:
                    # return the entire line as a token
                    self.tok = Token(Token.Match.LINE, s, lno, s)
                    return self.tok

            matchEnd = start # current end of match
            for match in Token.Match.values():
                cpat = match.cPattern
                if cpat == None:
                    break # nothing matches, so can't find a token
                if match.tokType == Token.TokType.SKIP and matchFound != None:
                    continue # ignore skips if we have a pending token
                if start != 0 and match.pattern[0] == '^':
                    continue # '^' must match at start of line
                m = re.match(cpat, s)
                m.pos = 0
                m.endpos = end
                if m:
                    e = m.endpos
                    if e == start:
                        continue # empty match, so try next pattern
                    if match.tokType == Token.TokType.SKIP:
                        # there's a non-empty skip match,
                        # so we skip over the matched part
                        # and get more stuff to read
                        start = e
                        continue LOOP
                    if matchEnd < e:
                        # found a longer match -- keep it!
                        matchEnd = e
                        matchString = m.group()
                        matchFound = match           
            if matchFound == None: # got to $ERROR, so nothing matches!!
                ch = s[start+1] # grab the char and advance
                sch = None
                if ch >= ' ' and ch <= '~':
                    sch = '"{}"'.format(ch)
                else
                    sch = '%04x'.format((int)ch)
                self.tok = Token(Token.Match.ERROR, "!ERROR("+sch+")", lno, s)
                return self.tok
            start = matchEnd # start of next token match
            # matchString is the matching string
            self.tok = Token(matchFound, matchString, lno, s) # persistent
            # System.out.println(String.format("match=%s\n", toggle));
            if matchFound.tokType == Token.TokType.LINE_TOGGLE:
                # System.out.println("going to line mode...");
                start = end # swallow the rest of the line
                self.lineMode = self.tok
            return self.tok

    def adv(self):
        # if we have already advanced past the current token,
        # we'll have to do it again
        if self.tok == None:
            cur()
        self.tok = None

    def put(self, t):
        raise PLCCException("PLCC Scan error", "put not implemented")

    # See if the expected token match is the same as the match
    # of the current token
    def match(self, match, trace):
        t = cur()
        mcur = t.match # the token we got
        if match == mcur: # compare the match expected with the token we got
            if trace != None:
                trace.print(t)
            adv()
        else:
            msg = "expected token " + match + ", got " + t.errString()
            raise PLCCException ("Parse error", msg)
        return t

    def isEOF(self):
        return cur().isEOF()

    def printTokens(self):
        while self.hasNext():
            t = next()
            s = None
            match t.match:
                case ERROR:
                    s = t.toString()
                    break
                case _:
                    s = "{} '{}'".format(t.match.toString(), t.toString())
            print("%4d: %s".format("%4d: %s", lno, s))

    def hasNext():
        return not cur().isEOF()

    def next():
        t = cur()
        adv()
        return t

if __name__ == __main__:
    rdr = None
    if len(sys.argv) == 0:
        rdr = io.BufferedReader(io.TextIO(sys.stdin))
    elif len(sys.argv) == 1:
        try:
            rdr = io.BufferedReader(io.TextIO(args[0]))
        except Exception as e:
            print(e.message + '\n')
            sys.exit()
    else:
        print("usage: Scan [filename]", file=sys.stderr)
        sys.exit()
    scn = Scan(rdr)
    scn.printTokens()
