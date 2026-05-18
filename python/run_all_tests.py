import glob
import importlib

def main():
    for filename in glob.glob("test_*.py"):
        module_name = filename[:-3]
        module = importlib.import_module(module_name)
        module.run_tests()

main()
