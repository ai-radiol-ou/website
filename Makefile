.PHONY: develop

dist/index.html: src/publications.html
	NODE_OPTIONS=--openssl-legacy-provider npm run build

src/publications.html: data/publications.xlsx
	python3 script/publications.py -i data/publications.xlsx -o src/publications.html

develop: src/publications.html
	NODE_OPTIONS=--openssl-legacy-provider npm run check

build: dist/index.html
	NODE_OPTIONS=--openssl-legacy-provider npm run build

clean:
	rm -rf dist && git checkout dist