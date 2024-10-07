.PHONY: update-deps
update-deps:
	@pip-compile requirements-dev.in
	@pip install -r requirements-dev.txt
	@pip-compile requirements.in
	@pip install -r requirements.txt

.PHONY: format-code
format-code:
	@poetry run pre-commit run --all-files --hook-stage pre-push --show-diff-on-failure

.PHONY: format-code
run-tests:
	@poetry run pytest tests  -s -vv --cov=lib --cov-report=term-missing --cov-fail-under=30
