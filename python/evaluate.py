def is_cons(form):
    if type(form) == list:
        return True
    else:
        return False

def get_car(compound_form):
    return compound_form[0]

def get_cdr(compound_form):
    return compound_form[1:]

def is_symbol(element):
    return True

def handle_operator(environment, operator_name, cdr):
    assert operator_name == "format"
    print(cdr[1])

def evaluate_compound_form(environment, form):
    car = get_car(form)
    cdr = get_cdr(form)
    if is_symbol(car):
        return handle_operator(environment, car, cdr)
    else:
        assert False

def evaluate(environment, form):
    if is_cons(form):
        evaluate_compound_form(environment, form)
