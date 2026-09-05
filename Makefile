.PHONY: sync serve validate test

sync:
	python3 sync.py

serve:
	python3 -m http.server 8000

validate:
	xmllint --noout sitemap.xml
	xmllint --noout feed.xml
	python3 scripts/validate.py

test:
	python3 -m unittest discover -s tests -v
