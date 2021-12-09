PYTHON=python3.8
SRC_DIRECTORIES=dt tests
COVERAGE_HTML_PATH=$(CURDIR)/htmlcov/index.html
UNIT_TEST_DIR=tests/unit
INTEGRATION_TEST_DIR=tests/integration

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
	${PYTHON} -m unittest discover -s ${UNIT_TEST_DIR}

ctest:
	coverage run  -m unittest discover -s ${UNIT_TEST_DIR}
	coverage report
	coverage html
	@echo "Full coverage report at: ${COVERAGE_HTML_PATH}"

itest:
	${PYTHON} -m unittest discover -s ${INTEGRATION_TEST_DIR}

lint:
	flake8 ${SRC_DIRECTORIES}

lint-fix:
	isort ${SRC_DIRECTORIES}
	autopep8 --in-place -r ${SRC_DIRECTORIES} --max-line-length 120 -a
	make lint

type-check:
	mypy --strict ${SRC_DIRECTORIES}

dry-run: lint type-check ctest itest

release: clean develop dry-run
