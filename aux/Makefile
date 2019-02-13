help:
	@echo 'Usage: make [target]'
	@echo
	@echo 'Targets:'
	@echo '  2019  Create printable PDF for 2019 C program and output.'
	@echo '  help  Show this help message.'

2019: clean
	pdflatex print-2019-02-14.tex
	make view FILE=print-2019-02-14.pdf
	make clean

view:
	if command -v xdg-open > /dev/null; then \
	    xdg-open "$(FILE)"; \
	elif command -v open > /dev/null; then \
	    open "$(FILE)"; \
	else \
	    echo Cannot find xdg-open or open.; \
	fi

clean:
	rm -rf *.log *.aux
