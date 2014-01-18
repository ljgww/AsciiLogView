#Ascii Log View

Text file viewer written in Python and TK.

Primary idea is to demonstrate use of TK in Python, using various widgets.


## Purpose

I work a lot with textual log files on windows. Default windows text viewer is Notepad. However, if you are afraid you may
accidentally overwrite something in notepad and damage log file integrity, you do not have much of an alternative.

I wanted a simple view tool with ability to copy sections of text (and eventually even alter some text before copying).



## X-Platform

To my knowing this code shall work on Windows, Linux and OSX - as is - with no modifications.
Since it is written in Python you need Python with TK installed for your platform.

If you are testing it yourself, I will be glad to hear your experience.


## Executable

It is possible to make executable from this source.

### Windows

Install Py2Exe to your Python. http://www.py2exe.org/

If needed adjust BuildWinExe.bat

Execute BuildWinExe.bat

Executable version would be in dist folder. Check Py2exe documentation.
