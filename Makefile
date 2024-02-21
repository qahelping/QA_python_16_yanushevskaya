test:
	@echo "Starting tests..."
	python -m pytest -m bbc --headless=no --alluredir allure-results

test_firefox:
	python -m pytest -m bbc --browser=firefox