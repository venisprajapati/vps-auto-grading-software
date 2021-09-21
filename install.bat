@echo off
python -m venv env
CALL env/Scripts/activate.bat
python -m pip install --upgrade pip
mkdir uploads
cd uploads
mkdir omrs
cd ..
"env/Scripts/pip.exe" install -r requirements.txt
pause
