# ./Makefile

SHELL := /bin/bash

setup: install configure

install:
	@echo "Installing Dufur backend app..."
	@echo "Setting up requirements..."
	pip install virtualenv
	virtualenv venv --python 3.11.9
	@echo "Installing required Python modules..."
	source venv/bin/activate && pip install --require-virtualenv --requirement requirements.txt

configure:
	@echo "Creating secret token file..."
	touch ./orchestrator/assets/key.sct
	@echo "Setting up secret token file..."
	@echo $(DOPPLER_KEY) > ./orchestrator/assets/key.sct
