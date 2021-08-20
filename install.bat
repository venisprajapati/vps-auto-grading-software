@echo off
python -m venv env
CALL env/Scripts/activate.bat
"env/Scripts/pip.exe" install -r requirements.txt
pause