import build_system
import sys

def get_file_content(filename):
    with open(filename) as f:
        return f.read()

def main(filename):
    filename = argv[1]

    contents = get_file_content(filename)
    stream = streams.create(contents)

    environment = {}
    form = read.read(stream)
    while form:
        evaluate.evaluate(environment, form)
        form = read.read(stream)

    read, eval_, print_ = build_system.build_system(filename)
    repl.repl(read, eval_, print)

main(sys.argv[1])
