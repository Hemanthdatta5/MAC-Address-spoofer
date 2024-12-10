DIST=dist

all: program extra

program: build
	pyinstaller ./*.py

extra: build
	cp LICENSE $(DIST)/
	cp docs $(DIST)/

build:
	mkdir -p $(DIST)

clean:
	rm -rf $(DIST)/*
	pyinstaller --clean

.PHONY: build clean