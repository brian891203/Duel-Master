# Duel-Master

## Getting Started

### Frontend

1. install pnpm
    ```bat
    npm install -g pnpm
    ```

2. clone
    ```bat
    git clone git@github.com:RogelioKG/Duel-Master.git
    ```

3. copy [this directory] to `src/assets/yugioh-card`

4. install dependencies
    ```bat
    cd Duel-Master
    pnpm install
    ```

5. run
    ```bat
    pnpm dev
    ```

### Backend

#### Using `poetry`
1. run
    ```bat
    backend/scripts/run.bat
    ```

#### Using `pip`
1. create virtual environment
   ```bat
   cd backend
   python -m venv .
   ```
2. activate virtual environment
   ```bat
   ./Scripts/activate
   ```

4. install dependencies
   ```bat
   pip install -r requirements.txt
   ```

5. run
   ```bat
   python app.py
   ```

[this directory]: https://github.com/kooriookami/yugioh-card/tree/master/src/assets/yugioh-card
