BUILD_DIR=$(PWD)/build
TEX=$(BUILD_DIR)/resume.tex
PDF=$(BUILD_DIR)/resume.pdf
MD=$(BUILD_DIR)/resume.md
HTML=$(BUILD_DIR)/resume.html
YAML_FILES=cv.yaml
BASE=$(PWD)
CSS_DIR=$(BASE)/css
CSS=$(CSS_DIR)/main.css
IMG_DIR=$(BASE)/img
SITE_DIR?=$(BASE)/_site

.PHONY: all pdf markdown css html site serve

all: $(PDF) $(HTML) $(MD)

markdown: $(MD)

site: $(SITE_DIR)

serve: $(SITE_DIR)
	cd $(SITE_DIR); \
	python ../scripts/run_server.py

html: $(HTML) $(CSS)

css: $(CSS)

pdf: $(PDF) $(TEX)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(CSS_DIR):
	mkdir -p $(CSS_DIR)

$(SITE_DIR): $(HTML) $(CSS)
	mkdir -p $(SITE_DIR)
	cp $(HTML) $(SITE_DIR)/index.html
	cp -r $(CSS_DIR) $(SITE_DIR)
	cp -r $(IMG_DIR) $(SITE_DIR)

$(TEX):
	python ./src/generate.py tex

$(MD):
	python ./src/generate.py md

$(CSS): $(CSS_DIR)
	sass --update sass:css

$(HTML): $(CSS)
	python ./src/generate.py html

$(PDF): $(TEX) $(BUILD_DIR)
	cd $(BUILD_DIR); pdflatex $(TEX)

viewpdf: $(PDF)
	open $(PDF)

viewhtml: $(HTML) $(CSS)
	open $(HTML)

clean:
	rm -rf $(BUILD_DIR)/resume*
	rm -rf $(CSS_DIR)
	rm -rf $(SITE_DIR)
