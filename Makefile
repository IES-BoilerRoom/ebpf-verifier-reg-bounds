.PHONY: check ci
check:
	python3 selftests/run_alu64_range.py

ci:
	python3 selftests/run_alu64_range.py --strict-ci
