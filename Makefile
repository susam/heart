help:
	@echo 'Usage: make [target]'
	@echo
	@echo 'Targets:'
	@echo '  py-venv   Set up virtual Python environment.'
	@echo '  py-heart  Run Python program to plot heart.'
	@echo '  c-heart   Compile and run C program to print heart.'
	@echo '  help     Show this help message.'

py-venv:
	python3 -m venv ~/.venv/heart
	echo . ~/.venv/heart/bin/activate > venv
	. ./venv && pip install matplotlib

py-heart:
	. ./venv && python3 heart.py

c-heart:
	cc -std=c89 -Wall -Wextra -pedantic heart.c
	./a.out > heart-2019-02-14.txt
	@echo
	@cat heart-2019-02-14.txt
	@echo

clean:
	rm -f a.out
