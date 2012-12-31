@echo off

( 
    @cd /d "%~dp0" 
) && (
    set PYTHONSCRIPT="import os;execfile('uploader.py');"
) && (
    "..\local\proxy.exe"
)

@pause>NUL

@echo off

