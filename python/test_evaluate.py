import evaluate
from types import SimpleNamespace

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

def fake_get_macro_function(environment, form):
    def result(form):
        assert form == "macro"
        return "macro_output"
    return result

def fake_evaluate_function_form(environment, form):
    assert environment == "environment"
    assert form == "macro_output"
    return "value"

def test_evaluate_macro_form():
    n = SimpleNamespace(
        get_macro_function=fake_get_macro_function,
        evaluate_function_form=fake_evaluate_function_form
    )
    assert evaluate.evaluate_macro_form(n, "environment", "macro") == "value"

def test_evaluate():
    n = SimpleNamespace(
        is_symbol=fake_is_symbol,
        evaluate_symbol=fake_evaluate_symbol,
        is_cons=fake_is_cons,
        evaluate_compound_form=fake_evaluate_compound_form
    )
    assert evaluate.evaluate(n, "environment", "symbol") == "symbol_to_value"
    assert evaluate.evaluate(n, "environment", "cons") == "cons_to_value"
    assert evaluate.evaluate(n, "environment", "self_evaluating") == "self_evaluating"

def run_tests():
    test_evaluate_macro_form()
    test_evaluate()

    print("test_evaluate : passed")
