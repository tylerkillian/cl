import evaluate

def fake_is_symbol(form):
    return form == "symbol"

def fake_evaluate_symbol(environment, symbol):
    assert environment == "environment"
    assert symbol == "symbol"
    return "symbol_to_value"

def fake_is_cons(form):
    return form == "cons"

def fake_evaluate_compound_form(environment, compound_form):
    assert environment == "environment"
    assert compound_form == "cons"
    return "cons_to_value"

def test_evaluate():
    logic = {
        "is_symbol": fake_is_symbol,
        "evaluate_symbol": fake_evaluate_symbol,
        "is_cons": fake_is_cons,
        "evaluate_compound_form": fake_evaluate_compound_form,
    }
    assert evaluate.evaluate(logic, "environment", "symbol") == "symbol_to_value"
    assert evaluate.evaluate(logic, "environment", "cons") == "cons_to_value"
    assert evaluate.evaluate(logic, "environment", "self_evaluating") == "self_evaluating"

def run_tests():
    test_evaluate()

    print("test_evaluate : passed")
