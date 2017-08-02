BUILD_DIR=$(PWD)/build
TEX=$(BUILD_DIR)/resume.tex
PDF=$(BUILD_DIR)/resume.pdf
MD=$(BUILD_DIR)/resume.md
HTML=$(BUILD_DIR)/resume.html
YAML_FILES=cv.yaml
BASE=$(PWD)
CSS_DIR=$(BASE)/css
CSS=$(CSS_DIR)/main.css

.PHONY: all pdf markdown css html

all: $(PDF) $(HTML) $(MD)

markdown: $(MD)

html: $(HTML) $(CSS)

css: $(CSS)

pdf: $(PDF) $(TEX)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(CSS_DIR):
	mkdir -p $(CSS_DIR)

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
