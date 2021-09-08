# Commands to generate the website HTML and clean up the environment

BUILDDIR=_build
.PHONY: help clean html linkcheck serve

html:
	sphinx-build -b html . $(BUILDDIR)/html

help:
	@echo
	@echo "Please use \"make <target>\" where <target> is one of:"
	@echo "  html       make the HTML files from the existing sources"
	@echo "  linkcheck  check all external links for integrity"
	@echo "  clean      delete all generated files"

clean:
	rm -rfv $(BUILDDIR)/*

linkcheck:
	sphinx-build -b linkcheck . $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."
serve: html
	python serve.py
