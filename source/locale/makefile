.PHONY: all messages clean

ifeq ($(OS),Windows_NT)
CHAIN = &
PYBABEL = C:\Python27\Scripts\pybabel.exe
MSGFMT = C:\Program Files (x86)\gettext-iconv\bin\msgfmt.exe
else
CHAIN = &&
PYBABEL = pybabel
MSGFMT = msgfmt
endif

LOCALES = en ru
PO = LC_MESSAGES/messages.po
MO = LC_MESSAGES/messages.mo

all:
	$(foreach L,$(LOCALES),"$(MSGFMT)" $(L)/$(PO) -o $(L)/$(MO) $(CHAIN))

messages:
	$(foreach L,$(LOCALES),"$(PYBABEL)" update -i messages.pot -d . -l $(L) $(CHAIN))
