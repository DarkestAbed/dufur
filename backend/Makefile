exec:
	@python main.py

remote-exec:
	@doppler run -- python main.py

reqs:
	@bash $(shell pwd)/reqs_install.sh

install:
	@pip install -r requirements.txt

setup: reqs install
