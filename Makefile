NAME		:= main
TEXRULE		:= latexmk -pdf -xelatex="xelatex -synctex=1 -interaction=batchmode" -use-make
BIB			:= $(HOME)/library.bib
DERIVED_BIB := references.bib

all: $(NAME).pdf $(DERIVED_BIB)

$(NAME).pdf: $(NAME).tex $(BIB)
	$(TEXRULE) $< 

cleanall:
	latexmk -C 

clean:
	latexmk -c

# With bibtex
#$(DERIVED_BIB): $(NAME).aux $(BIB) 
#	bibexport -o $@ $<

# With biber
$(DERIVED_BIB): $(NAME).aux
	biber --output-format=bibtex \
		  --output-fieldcase=lower \
		  --output-file $@ \
		  --output-resolve $(NAME).bcf

