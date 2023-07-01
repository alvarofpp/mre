# Variables
PACKAGE_NAME=mre
DOCKER_IMAGE_LINTER=alvarofpp/python:linter
ROOT=$(shell pwd)
LINT_COMMIT_TARGET_BRANCH=origin/main

## Test
TEST_CONTAINER_NAME=${PACKAGE_NAME}_test
TEST_COMMAND=coverage run -m unittest discover tests

# Commands
.PHONY: build
build: install-hooks
	@docker build -t ${PACKAGE_NAME} .

.PHONY: build-no-cache
build-no-cache: install-hooks
	@docker build --no-cache -t ${PACKAGE_NAME} .

.PHONY: install-hooks
install-hooks:
	git config core.hooksPath .githooks

.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-commit ${LINT_COMMIT_TARGET_BRANCH} \
		&& lint-markdown \
		&& lint-yaml \
		&& lint-python"

.PHONY: test
test:
	@docker run --rm -v ${ROOT}:/app \
		--name ${TEST_CONTAINER_NAME} ${PACKAGE_NAME} \
		${TEST_COMMAND}

.PHONY: test-coverage
test-coverage:
	@docker run --rm -v ${ROOT}:/app \
		--name ${TEST_CONTAINER_NAME} ${PACKAGE_NAME} \
		/bin/bash -c "${TEST_COMMAND} && coverage report -m"
