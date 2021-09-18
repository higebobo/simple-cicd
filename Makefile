MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := test

# all targets are phony
.PHONY: $(shell egrep -o ^[a-zA-Z_-]+: $(MAKEFILE_LIST) | sed 's/://')

ifneq ("$(wildcard ./.env)","")
  include ./.env
endif

pip: ## Install package by pip
	@pip install -r requirements.txt

test: test-quiet ## Run test

test-quiet: ## Run test quiet
	@py.test -s

test-verbose: ## Run test verbose
	@py.test -s --verbose

deploy: test deploy-all  ## Deploy all environments with test

deploy-all: deploy-test deploy-stage deploy-prod ## Deploy all environments

deploy-mock: ## Deploy mock environment
	@fab mock

deploy-test: ## Deploy testing environment
	@fab test deploy

deploy-stage: ## Deploy staging environment
	@fab stage deploy

deploy-prod: ## Deploy production environment
	@fab prod deploy

help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
