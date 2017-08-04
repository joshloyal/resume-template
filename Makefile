CUR_DIR=$(CURDIR)
BUILD_DIR=$(CUR_DIR)/build
TEX=$(BUILD_DIR)/resume.tex
PDF=$(BUILD_DIR)/resume.pdf
MD=$(BUILD_DIR)/resume.md
HTML=$(BUILD_DIR)/resume.html
CODE=$(BUILD_DIR)/code.html
YAML_FILES=cv.yaml
CSS_DIR=$(CUR_DIR)/css
CSS=$(CSS_DIR)/main.css
IMG_DIR=$(CUR_DIR)/img
SITE_DIR?=$(CUR_DIR)/_site


.PHONY: all pdf markdown css html site serve

all: $(PDF) $(HTML) $(MD)

markdown: $(MD)

site: $(SITE_DIR)

serve: $(SITE_DIR)
	cd $(SITE_DIR); \
	python $(CUR_DIR)/scripts/run_server.py

html: $(HTML) $(CSS)

css: $(CSS)

pdf: $(PDF) $(TEX)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(CSS_DIR):
	mkdir -p $(CSS_DIR)

$(SITE_DIR): $(HTML) $(CSS)
	mkdir -p $(SITE_DIR)
	mkdir -p $(SITE_DIR)/code
	cp $(HTML) $(SITE_DIR)/index.html
	cp $(CODE) $(SITE_DIR)/code/index.html
	cp -r $(CSS_DIR) $(SITE_DIR)
	cp -r $(IMG_DIR) $(SITE_DIR)

$(TEX):
	python $(CUR_DIR)/src/generate.py tex

$(MD):
	python $(CUR_DIR)/src/generate.py md

$(CSS): $(CSS_DIR)
	sass --update sass:css

$(HTML): $(CSS)
	python $(CUR_DIR)/src/generate.py html

$(PDF): $(TEX) $(BUILD_DIR)
	cd $(BUILD_DIR); pdflatex $(TEX)

viewpdf: $(PDF)
	open $(PDF)

viewhtml: $(HTML) $(CSS)
	open $(HTML)

clean:
	rm -rf $(BUILD_DIR)/resume*
	rm -rf $(CSS_DIR)
	rm -rf $(SITE_DIR)/index.html
	rm -rf $(SITE_DIR)/code/index.html
	rm -rf $(SITE_DIR)/css/*
	rm -rf $(SITE_DIR)/img/*
