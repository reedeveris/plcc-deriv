# Process command-line arguments (flags, filenames) from the given args
# Read programs from named files and then from standard input.
# If the '-n' flag is given, don't prompt for standard input,
#     otherwise prompt with "--> "
# If the '-t' command line argument is given, toggle the trace feature
#     (defaults to no trace)
# For each input program, use 'action' to parse the input
#     and act on the resulting parse tree
import sys
import io

class ProcessFiles():

    # build a parse tree and act on it
    def action(scn, trace):
        pass

    def processFile(scn, trace, prompt, prog):
        try:
            # read and process programs from this 
            while True:
                print(prompt)
                if scn.isEOF():
                    break
                if trace != None:
                    trace.reset()
                if prog != None:
                    print(prog)
                    if trace != None:
                        print('\n')
                action(scn, trace)
        except Error as e:
            print(e.getMessage() + '\n')
            System.err.println(e)
            sys.exit()

    def processFiles(args):
        trace = None
        # first read and process any input files from the command line
        scn = None
        prog = None
        prompt = "--> "
        for i in range(args.length):
            s = args[i]
            if s == "-n":
                # turns off prompts when reading from stdin
                prompt = ""
                continue
            if s == "-t":
                # toggle traces
                trace = Trace() if trace == null else None
                continue
            if s == "-v":
                # toggle verbose cmd line name output
                prog = ""  if prog == null else None
                continue
            try:
                scn = Scan(io.BufferedReader(io.TextIO(s)))
            except FileNotFoundError:
                print(s + ": no such file ... exiting\n")
                sys.exit()
            if prog != None:
                prog = "[" + s + "]"
            processFile(scn, trace, "", prog)
        # finally read and process programs from standard input
        rdr = io.BufferedReader(io.TextIO(sys.stdin))
        scn = Scan(rdr)
        if prog != None:
            prog = "[stdin]"
        processFile(scn, trace, prompt, prog)

