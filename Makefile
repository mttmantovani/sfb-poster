NAME		:= main
THEME		:= themeKonstanz.sty
TEXRULE		:= latexmk -pdf -pdflatex="xelatex -synctex=1 -interaction=batchmode" -use-make
BIB			:= $(HOME)/library.bib
DERIVED_BIB := references.bib

all: $(NAME).pdf $(DERIVED_BIB)

$(NAME).pdf: $(NAME).tex $(THEME) $(BIB)
	$(TEXRULE) $< 

cleanall:
	latexmk -C 

clean:
	latexmk -c

# With bibtex
#$(DERIVED_BIB): $(NAME).aux $(BIB) 
#	bibexport -o $@ $<

# With biber
$(DERIVED_BIB): $(NAME).bbl
	biber --output-format=bibtex \
		  --output-fieldcase=lower \
		  --output-file $@ \
		  --output-resolve $(NAME).bcf

