TEST = pytest 
TEST_ARGS = --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
UNIT_TEST = pytest
STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive

.PHONY: all
# all: style-check type-check run-test clean
all: style-check type-check unit_test clean

.PHONY: type-check
type-check:
	$(TYPE_CHECK) .
	@echo "Type check completed successfully"

.PHONY: style-check
style-check:
	$(STYLE_CHECK) .
	@echo "Style check completed successfully"

.PHONY: unit_test
unit_test:
	$(UNIT_TEST) .

# discover and run all tests
# .PHONY: run-test
# run-test:
# 	$(TEST) $(TEST_ARGS) .

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis


.PHONY: push
push: run-test clean
	

.PHONY: fix-style
fix-style:
	$(STYLE_FIX) .
