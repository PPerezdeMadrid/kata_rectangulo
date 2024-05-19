
all: execute

compile: clean
	gcc -o ejecutable test_bolos.c
	
execute: compile
	./ejecutable

clean:
	rm -f ./ejecutable

cantidad:
	grep -o -i 'test' test_bolos.c | wc -l | awk '{print int($$1/2)}'
