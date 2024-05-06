install-dependencies:
	pip install -r requirements.txt

run-selenium-tests:
	pytest -k test_login.py

run-playwright-tests:
	pytest -k test_challenges.py --headed

run-api-tests:
	pytest -k test_api.py 

run-all-tests: run-selenium-tests run-playwright-tests run-api-tests
