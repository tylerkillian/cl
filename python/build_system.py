import evaluate
import read
import streams

def build_stream(filename):
    return streams.create_from_file(filename)

def build_environment():
    return {}

def build_read(stream):
    def _read():
        return read.read(stream)
    return _read

def build_eval_(environment):
    def _eval_(form):
        return evaluate.evaluate(environment, form)
    return _eval_

def build_system(filename):
    stream = build_stream(filename)

    environment = build_environment()

    read = build_read(stream)
    eval_ = build_eval_(environment)
    print_ = print

    return read, eval_, print_
