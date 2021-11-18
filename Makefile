PYTHON=python3
SRC_DIRECTORIES=dt tests

develop:
	${PYTHON} -m pip install -e .

clean:
	-${PYTHON} ./setup.py clean --all
	-find src -name '*.pyc' -exec rm {} \;
	-find src -name '*.pyo' -exec rm {} \;
	-find tst -name '*.pyc' -exec rm {} \;
	-find tst -name '*.pyo' -exec rm {} \;
	-find . | grep -E "__pycache__" | xargs rm -rf
	-find . | grep -E "async_dns_trawler.egg-info" | xargs rm -rf
	-rm -rf .pytest_cache
	-rm .coverage

test:
	${PYTHON} -m unittest discover -s tests

ctest:
	coverage run --branch --omit="tests/*" -m unittest discover -s tests/unit
	coverage report
	coverage html

lint:
	flake8 ${SRC_DIRECTORIES}

lint-fix:
	autopep8 --in-place -r ${SRC_DIRECTORIES} --max-line-length 120
	make lint

type-check:
	mypy --strict ${SRC_DIRECTORIES}

release: clean develop lint type-check ctest
