install-dependencies:
	pip3 install -r requirements.txt

run-selenium-tests:
	python3 -m pytest -m selenium --pdb $(if $(HEADLESS),HEADLESS=$(HEADLESS),)

run-playwright-tests:
	python3 -m pytest -k playwright $(if $(HEADLESS),,--headed)

run-api-tests:
	python3 -m pytest -k test_api.py 

run-all-tests: run-selenium-tests run-playwright-tests run-api-tests
