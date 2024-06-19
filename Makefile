install-dependencies:
	pip install -r requirements.txt

run-selenium-tests:
	pytest -m selenium

run-playwright-tests:
	pytest -k playwright $(if $(HEADLESS),,--headed)

run-api-tests:
	pytest -k test_api.py 

run-all-tests: run-selenium-tests run-playwright-tests run-api-tests
