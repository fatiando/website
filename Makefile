# Commands to generate the website HTML and clean up the environment
.PHONY: help clean html linkcheck serve

html:
	nene

help:
	@echo
	@echo "Please use \"make <target>\" where <target> is one of:"
	@echo "  html       make the HTML files from the existing sources"
	@echo "  serve      start a server and automatically update if sources change"
	@echo "  clean      delete all generated files"

clean:
	rm -rfv _build

serve:
	nene --serve
