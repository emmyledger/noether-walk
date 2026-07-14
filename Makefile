PY ?= .venv/bin/python

.PHONY: setup test tier0 tier0-formation verdicts leakcheck

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e ".[dev]"

test:
	$(PY) -m pytest -q

tier0:
	$(PY) -m invariants.tier0 --arc installed

tier0-formation:
	$(PY) -m invariants.tier0 --arc formation

verdicts:
	$(PY) -m invariants.verdicts artifacts
