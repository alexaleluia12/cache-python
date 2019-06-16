run:
	pipenv run python -u application.py
test:
	pytest --cov=app --cov-report=term-missing
html-coverage:
	coverage html
lint:
	pycodestyle --show-source app