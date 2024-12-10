BUILD=dist

all: program extra

program: build
	pyinstaller ./*.py

extra: build
	cp LICENSE $(BUILD)/
	cp docs $(BUILD)/

build:
	mkdir -p $(BUILD)

clean:
	rm -rf $(BUILD)/*

.PHONY: build clean