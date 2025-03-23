@REM :: create virtual environment
@REM if not exist .venv (
@REM   python -m venv .venv
@REM )

:: activate virtual environment
call .venv\Scripts\activate

@REM :: install dependencies
@REM pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
@REM pip install -r requirements.txt

:: run the app
python app.py
