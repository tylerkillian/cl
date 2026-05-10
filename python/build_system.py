RULES = {
    "main": [
        "read",
        "eval",
        "print"
    ],
}
def build_system(filename):
    dependencies = {}

    contents = get_file_content(filename)
    stream = streams.create(contents)

    environment = {}
    form = read.read(stream)
    while form:
        evaluate.evaluate(environment, form)
        form = read.read(stream)

    return read, eval_, print_
