@echo off
cd .\flask app
set FLASK_APP=app
pip install pipwin
pipwin install pyaudio
pip install -r requirements.txt
python -m flask run
pause