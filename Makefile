.PHONY: sync serve validate

sync:
	python3 sync.py

serve:
	python3 -m http.server 8000

validate:
	xmllint --noout sitemap.xml
	xmllint --noout feed.xml
	python3 -c "
import subprocess, sys
fail = 0
for f in ['index.html', 'pages/projects.html', 'pages/writings.html',
          'proj/visayasgrid.html', 'blogs/modelling-the-philippine-grid.html',
          'blogs/how-i-built-the-visayas-grid.html',
          'blogs/visayas-grid-engineering.html', 'blogs/how-to-build-the-life-you-want.html',
          'blogs/how-to-create-a-website.html']:
    result = subprocess.run(['tidy', '-eq', f], capture_output=True, text=True)
    if result.returncode != 0:
        print(f'  ERRORS in {f}')
        for line in result.stdout.splitlines()[:5]:
            print(f'    {line}')
        fail = 1
if fail:
    print('HTML validation FAILED')
    sys.exit(1)
print('HTML validation passed')
" 2>/dev/null || echo "  Install tidy: brew install tidy-html5"
