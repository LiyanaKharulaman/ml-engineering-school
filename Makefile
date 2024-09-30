.PHONY: update-deps
update-deps:
	@pip-compile requirements-dev.in
	@pip install -r requirements-dev.txt
	@pip-compile requirements.in
	@pip install -r requirements.txt

.PHONY: format-code
format-code:
	@pre-commit run --all-files --hook-stage pre-push --show-diff-on-failure
