import evaluate
import read
import streams
import sys

def get_file_content(filename):
    with open(filename) as f:
        return f.read()

def main(argv):
    filename = argv[1]

    contents = get_file_content(filename)
    stream = streams.create(contents)

    environment = {}
    form = read.read(stream)
    while form:
        evaluate.evaluate(environment, form)
        form = read.read(stream)

main(sys.argv)
