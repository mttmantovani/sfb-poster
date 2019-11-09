# Makefile for Fig. 3

PROJDIR	:= ../..
FIGNAME	:= $(notdir $(shell pwd))
TEXRULE	:= latex -interaction=batchmode
REDIR	:= > /dev/null 2>&1
DEBUG	?= 0
TOCLEAN    = .ovp .pfx .ps .dvi .aux .log
TOCLEANALL = $(TOCLEAN) .eps .pdf
ifeq (1, $(DEBUG))
REDIR	:=
endif

.PHONY: clean cleanall

all: $(FIGNAME).pdf
	@cp $^ $(PROJDIR)

$(FIGNAME).pdf: $(FIGNAME).eps $(FIGNAME).tex
	@$(TEXRULE) $(FIGNAME).tex $(REDIR) \
	&& dvips $(FIGNAME).dvi $(REDIR) \
	&& ps2pdf $(FIGNAME).ps $(REDIR)

$(FIGNAME).eps: $(FIGNAME).py
	@python $< --processing $(REDIR) 
	@python unglyph.py $(FIGNAME).eps $(FIGNAME).eps $(REDIR)

clean:
	@rm -f $(addprefix $(FIGNAME),$(TOCLEAN)) $(REDIR)

cleanall:
	@rm -f $(addprefix $(FIGNAME),$(TOCLEANALL)) $(REDIR)
