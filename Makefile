install-dependencies:
	pip3 install -r requirements.txt

install-typescript-dependencies:
	cd playwright_typescript_tests && npm install && npm run install:browsers

install-all-dependencies: install-dependencies install-typescript-dependencies

run-selenium-tests:
	python3 -m pytest -m selenium --pdb $(if $(HEADLESS),HEADLESS=$(HEADLESS),)

run-playwright-tests:
	python3 -m pytest -k playwright $(if $(HEADLESS),,--headed)

run-api-tests:
	python3 -m pytest -k test_api.py 

run-typescript-tests:
	cd playwright_typescript_tests && npm test

run-all-tests: run-selenium-tests run-playwright-tests run-api-tests

run-all-tests-including-typescript: run-selenium-tests run-playwright-tests run-api-tests run-typescript-tests
