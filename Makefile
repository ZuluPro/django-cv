clean:
	rm -rf django_cv.egg-info/ build/ dist/ coverage_html_report .coverage

test:
	python setup.py test

install:
	python setup.py install

build:
	python setup.py build

register:
	bash register.sh
