import sys

class Rep(ProcessFiles):

    # Parse the program and call $run() on the resulting parse tree
    def action(Scan scn, Trace trace)
        _Start.parse(scn, trace).$run()

   
# Run programs from command-line files
# and then perform a read-eval-print loop on programs
# read from standard input.
if __name__ ==  __main__:
    new Rep().processFiles(sys.argv[1:])
