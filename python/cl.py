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
    code = read.read(None, stream)
    while code:
        print("code =", code)
        code = read.read(None, stream)

main(sys.argv)
