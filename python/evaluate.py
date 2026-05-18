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

def evaluate_macro_form(n, environment, form):
    macro_function = n.get_macro_function(environment, form)
    replacement_form = macro_function(form)
    return n.evaluate_function_form(environment, replacement_form)

def evaluate_compound_form(environment, form):
    car = get_car(form)
    cdr = get_cdr(form)
    if is_symbol(car):
        return handle_operator(environment, car, cdr)
    else:
        assert False

def evaluate(n, environment, form):
    if n.is_symbol(form):
        return n.evaluate_symbol(environment, form)
    elif n.is_cons(form):
        return n.evaluate_compound_form(environment, form)
    else:
        return form
