@echo off
CALL env/Scripts/activate.bat
"env/Scripts/python.exe" app.py %*
pause