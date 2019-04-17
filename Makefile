.PHONY : clean


init:
	pip install -r requirements.txt

venv:
	python3 -m virtualenv virtualenv

test:
	( \
		python3 -m virtualenv ./virtualenv; \
		. ./virtualenv/bin/activate; \
		pip3 install -r requirements.txt; \
		python tests; \
		deactivate; \
	)

lint:
	pyflakes src/*.py
	pyflakes tests/*.py
	pylint src/*.py
	pylint tests/*.py

coverage:
	coverage run -a --omit */virtualenv/* src/__init__.py
	coverage run -a --omit */virtualenv/* src/main.py
	coverage run -a --omit */virtualenv/* tests

build:
	( \
		python3 -m virtualenv ./virtualenv; \
		. ./virtualenv/bin/activate; \
		pip3 install -r requirements.txt; \
		python src/main.py; \
		deactivate; \
	)

clean:
	-rm -fr Reports
	-rm -fr virtualenv
	-rm CloudFormation.json
	-rm .coverage