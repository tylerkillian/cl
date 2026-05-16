import glob
import importlib

print("a0")
d1 = {
    "f1": lambda x: print("d1 hello", x),
    "f2": lambda x: print("d1 hello again", x)
}
d2 = {
    "f1": lambda x: print("d2 hello", x),
    "f2": lambda x: print("d2 hello again", x)
}
code = """
def doit(another):
    f1("tyler")
    f2("killian")
    f1(another)
doit("yo")
"""
exec(code, d1)
exec(code, d2)
print("a1")

def main():
    for filename in glob.glob("test_*.py"):
        module_name = filename[:-3]
        module = importlib.import_module(module_name)
        module.run_tests()

main()
