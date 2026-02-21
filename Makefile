PYTHON = venv/bin/python
PORT   = 8000

build:
	$(PYTHON) build.py

serve: build
	$(PYTHON) -m http.server $(PORT) -d _site

stop:
	kill $(shell lsof -t -i:$(PORT))

clean:
	rm -rf _site

.PHONY: build serve clean
