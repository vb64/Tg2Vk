.PHONY: all messages clean

ifeq ($(OS),Windows_NT)
PYBABEL = C:\Python27\Scripts\pybabel.exe
MSGFMT = C:\Program Files (x86)\gettext-iconv\bin\msgfmt.exe
else
PYBABEL = pybabel
MSGFMT = msgfmt
endif

PO = LC_MESSAGES/messages.po
MO = LC_MESSAGES/messages.mo

all:
	$(MSGFMT) en/$(PO) -o en/$(MO)
	$(MSGFMT) ru/$(PO) -o ru/$(MO)

messages:
	$(PYBABEL) update -i messages.pot -d . -l en
	$(PYBABEL) update -i messages.pot -d . -l ru
