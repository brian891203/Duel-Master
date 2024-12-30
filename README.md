# Duel-Master

## Setting up this project

1. clone this repo
    ```
    git clone git@github.com:RogelioKG/Duel-Master.git
    ```

2. copy the contents of [this yugioh-card assets directory][yugioh card assets] to `backend/assets/yugioh-card`

## Frontend

### Using `npm`

1. install dependencies
    ```
    cd Duel-Master/frontend
    npm install
    ```

2. run
    ```
    npm run dev
    ```

### Using `pnpm`

1. install dependencies
    ```
    cd Duel-Master/frontend
    pnpm install
    ```

2. run
    ```
    pnpm dev
    ```

## Backend (testing)

### Using `poetry`
1. run

    + Windows
        ```bat
        scripts/run-backend.bat
        ```

    + Linux
        ```bash
        source scripts/run-backend.sh
        ```

### Using `pip`
1. run

    + Windows
        ```bat
        scripts/run-backend-pip.bat
        ```

    + Linux
        ```bash
        source scripts/run-backend.sh
        ```

## API Doc
### Translate API
  ```json
  [API]: /api/translate
  [HTTP method]: POST
  [Request Headers]:
    {
      "Content-Type": "multipart/form-data",
    }
  [Request Parameters]:
    {
      "image": formData
    }
  [Response (Success)]:
    {
      "success": true,
      "frontCardData": {
        "name": "灰流麗",
        "attribute": "fire",
        "level": 3,
        "monsterType": "不死族",
        "atk": 0,
        "def": 1800,
        "description": "「灰流麗」的效果...",
      },
    }
  [Response (Failure)]:
    {
      "success": false,
      "errMessage": "(翻譯過程出錯)",
    }
  ```
### Question API
  ```json
  [API]: /api/question
  [HTTP method]: POST
  [Request Headers]:
    {
      "Content-Type": "text/plain",
    }
  [Request Body]:
    text
  [Response (Success)]:
    {
      "success": true,
      "answer": "(問答結果)",
    }
  [Response (Failure)]:
    {
      "success": false,
      "errMessage": "(問答過程出錯)",
    }
  ```

### Assets: Material API
  ```json
  [API]: /api/assets/material
  [HTTP method]: POST
  [Request Headers]:
    {
      "Content-Type": "...",
    }
  [Request Body]:
    text
  [Response (Success)]:
    {
      "success": true,
      "answer": "(問答結果)",
    }
  [Response (Failure)]:
    {
      "success": false,
      "errMessage": "(問答過程出錯)",
    }
  ```

### Assets: Image API
  ```json
  [API]: /api/assets/image
  [HTTP method]: POST
  [Request Headers]:
    {
      "Content-Type": "...",
    }
  [Request Body]:
    text
  [Response (Success)]:
    {
      "success": true,
      "answer": "(問答結果)",
    }
  [Response (Failure)]:
    {
      "success": false,
      "errMessage": "(問答過程出錯)",
    }
  ```

[yugioh card assets]: https://github.com/kooriookami/yugioh-card/tree/master/src/assets/yugioh-card
