# Notes for setup Tg2Vk project on Windows

To install `make` for winfows, download setup [from here](http://gnuwin32.sourceforge.net/packages/make.htm). After installation, add folder with make.exe to system PATH.

To install `gettext` for windows, download setup [from here](https://mlocati.github.io/articles/gettext-iconv-windows.html).

Install Python 2.7.14 (recommended) [from here](https://www.python.org/downloads/).

Then edit next source files for correct path of installed programs:

`makefile` line:

```
PYBABEL = C:\Python27\Scripts\pybabel.exe
```

`source\locale\makefile` lines:

```
PYBABEL = C:\Python27\Scripts\pybabel.exe
MSGFMT = C:\Program Files (x86)\gettext-iconv\bin\msgfmt.exe
```
