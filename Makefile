
# values
CC= python3
LIBS=$(wildcard requirements.txt)
VERSION=1.0
PROG=main

default: 
	${CC} ${PROG}.py

install: ${PROG}.py
	@echo "----- START Instalation -----"
	@${CC} -m PyInstaller --onefile ${PROG}.py 
	@mv dist/${PROG} ${PROG}
	@rm -r dist build ${PROG}.spec __pycache__
	@echo "\nInstallation Complite!\n"

set:
	@pip install -r ${LIBS}
	@echo "\nRequirements are avaliable!\n"

