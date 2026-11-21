Set-Location (Split-Path -Parent $MyInvocation.MyCommand.Path)
python -m pip install -r requirements.txt
python tools\build_audio.py
