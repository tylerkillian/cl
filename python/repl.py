def repl(environment, read, eval_, print_):
    while True:
        form = read()
        if not form:
            break
        value = eval_(form)
        print_(value)
