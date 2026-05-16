import repl

def create_fake_read():
    forms = ["1", "2", "3"]
    def result():
        if forms:
            return forms.pop(0)
        else:
            return None
    return result

def fake_eval_(form):
    values = {
        "1": "one",
        "2": "two",
        "3": "three"
    }
    return values[form]

def create_fake_print_():
    log = []
    def fake_print_(value):
        log.append(value)
    return fake_print_, log

def run_tests():
    fake_read = create_fake_read()
    fake_print_, log = create_fake_print_()
    repl.repl(fake_read, fake_eval_, fake_print_)

    assert log == ["one", "two", "three"]

    print("test_repl : passed")
