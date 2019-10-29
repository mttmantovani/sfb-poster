# Makefile for Fig. 2

PROJDIR	   := ../..
FIGNAME	   := $(notdir $(shell pwd))
TEXRULE	   :=latex -interaction=batchmode 
DEBUG	   ?= 0
TOCLEAN    = .ovp .pfx .ps .dvi .aux .log
TOCLEANALL = $(TOCLEAN) .pdf .eps
REDIR	:= > /dev/null 2>&1
ifeq (1, $(DEBUG))
REDIR	   :=
endif

.PHONY: clean cleanall

all: $(FIGNAME).pdf
	@cp $^ $(PROJDIR)

$(FIGNAME).pdf: $(FIGNAME).tex $(FIGNAME).eps
	@$(TEXRULE) $< $(REDIR) \
	&& dvips $(FIGNAME).dvi $(REDIR) \
	&& ps2pdf $(FIGNAME).ps $(REDIR)

$(FIGNAME).eps: $(FIGNAME).py
	@python $< "processing=True" $(REDIR) 
	@chmod +x $(PROJDIR)/bin/unglyph
	@$(PROJDIR)/bin/unglyph $@ $@ $(REDIR)

clean:
	@rm -f $(addprefix $(FIGNAME),$(TOCLEAN)) $(REDIR)

cleanall:
	@rm -f $(addprefix $(FIGNAME),$(TOCLEANALL)) $(REDIR)

