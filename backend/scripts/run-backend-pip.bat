:: create virtual environment
if not exist .venv (
  python -m venv .venv
)

:: activate virtual environment
call .venv\Scripts\activate

:: install dependencies
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt

:: run the app
python app.py
