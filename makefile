.PHONY: all run media messages

ifeq ($(OS),Windows_NT)
PYBABEL = C:\Python27\Scripts\pybabel.exe
else
PYBABEL = pybabel
endif


S = source
LOCALEDIR = $(S)/locale
LIBDIR = $(S)/libs

all: run

run:
	make -C $(S)

flake8:
	python -m flake8 --max-line-length=110 --exclude=libs --builtins="_" $(S)

lint:
	python -m pylint $(S)/localhost.py $(S)/settings.py $(S)/telegram

media:
	make -C $(LOCALEDIR)

messages:
	$(PYBABEL) extract -F babel.cfg -o $(LOCALEDIR)/messages.pot .
	make -C $(LOCALEDIR) messages

setup: media
	python -m pip install -t $(LIBDIR) -r $(LIBDIR)/requirements.txt
	python -m pip install -r requirements.txt
