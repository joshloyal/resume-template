BUILD_DIR=$(PWD)/build
TEX=$(BUILD_DIR)/resume.tex
PDF=$(BUILD_DIR)/resume.pdf
MD=$(BUILD_DIR)/resume.md
YAML_FILES=cv.yaml
BASE=$(PWD)

.PHONY: all tex

all: $(PDF)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(TEX):
	python ./src/generate.py tex

$(PDF): $(TEX) $(BUILD_DIR)
	cd $(BUILD_DIR); pdflatex $(TEX)

viewpdf: $(PDF)
	open $(PDF)

clean:
	rm -rf $(BUILD_DIR)/resume*
