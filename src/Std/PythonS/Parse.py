import sys

class Parse(ProcessFiles):

    # Parse the program
    def action(scn, trace):
        _Start.parse(scn, trace)


# Read programs from command-line files
# and then read programs from standard input.
if __name__ == __main__:
    Parse().processFiles(sys.argv[1:])
