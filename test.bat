@echo off
CALL env/Scripts/activate.bat
"env/Scripts/python.exe" test.py %*
pause