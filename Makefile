install:
     poetry install

build: check
    poetry build

.PHONY: install build