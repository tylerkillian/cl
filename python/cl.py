import build_system
import repl
import sys

def main(filename):
    read, eval_, print_ = build_system.build_system(filename)
    repl.repl(read, eval_, print)

main(sys.argv[1])
