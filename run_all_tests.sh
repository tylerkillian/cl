set -e

clisp run-all-tests.lisp

COMPILERS=(
	"gcc -std=c90"
       	"g++" 
	"clang -std=c90" 
	"clang++ -x c"
)
for compiler in "${COMPILERS[@]}"
do
	$compiler -pedantic -Wall -Wextra -Werror -I./ -o run_all_tests *.c
	./run_all_tests run-all-tests.lisp
	rm run_all_tests
done
