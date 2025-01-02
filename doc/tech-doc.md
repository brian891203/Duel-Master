# Technical Documentation





## [▶️][0] Outline
+ **[Setup Guide][1]**
+ **[Running the Project][2]**
  + **[Frontend][2-1]**
  + **[Backend][2-2]**
+ **[Build][3]**
  + **[What][3-1]**
  + **[How][3-2]**
+ **[System Requirements Specification][4]**
  + **[Functional Requirements][4-1]**
  + **[Non Functional Requirements][4-2]**
+ **[API][5]**
  + **[Translate API][5-1]**
  + **[Question API][5-2]**
  + **[Card Material API][5-3]**
  + **[Card Image API][5-4]**

[0]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#%EF%B8%8F-outline
[1]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#%EF%B8%8F-setup-guide
[2]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#%EF%B8%8F-running-the-project
[2-1]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#frontend
[2-2]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#backend
[3]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#%EF%B8%8F-build
[3-1]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#what
[3-2]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#how
[4]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#%EF%B8%8F-system-requirements-specification
[4-1]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#functional-requirements
[4-2]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#non-functional-requirements
[5]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#%EF%B8%8F-api
[5-1]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#translate-api
[5-2]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#question-api
[5-3]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#card-material-api
[5-4]: https://github.com/RogelioKG/Duel-Master/blob/main/doc/tech-doc.md?tab=readme-ov-file#card-image-api





## [⬆️][0] Setup Guide

1. clone this repo
    ```
    git clone git@github.com:RogelioKG/Duel-Master.git
    ```

2. copy the contents of [yugioh-card-assets-directory] to [`backend/assets/card-material`]

    > 遊戲王卡材質包

3. copy the contents of [mt5-large-translation-for-yu-gi-oh-ja-traditional-zh] to [`backend/model`]

    > 翻譯模型 (注意：2.5 GB 左右，很胖)





## [⬆️][0] Running the Project

### Frontend

```
cd frontend
```

#### Using `npm`

1. install dependencies
    ```
    npm install
    ```

2. run (development)
    ```
    npm run dev
    ```

#### Using `pnpm`

1. install dependencies
    ```
    pnpm install
    ```

2. run (development)
    ```
    pnpm dev
    ```

### Backend

```
cd backend
```

#### Using `pip`
1. run

    + Windows
        ```bat
        scripts/run-backend-pip.bat
        ```

    + Linux
        ```bash
        source scripts/run-backend-pip.sh
        ```

#### Using `poetry`
1. run

    + Windows
        ```bat
        scripts/run-backend.bat
        ```

    + Linux
        ```bash
        source scripts/run-backend.sh
        ```

2. freeze the requirements
    ```
    poetry export --without-hashes --format=requirements.txt > requirements.txt
    ```

[`backend/assets/card-material`]: https://github.com/RogelioKG/Duel-Master/tree/main/backend/assets/card-material
[`backend/model`]: https://github.com/RogelioKG/Duel-Master/tree/main/backend/model
[yugioh-card-assets-directory]: https://github.com/kooriookami/yugioh-card/tree/master/src/assets/yugioh-card
[mt5-large-translation-for-yu-gi-oh-ja-traditional-zh]: https://huggingface.co/plutokokoa/mt5-large-translation-for-yu-gi-oh-ja-traditional-zh/tree/main





## [⬆️][0] Build

### What

前端程式碼可以打包成只有純 HTML / CSS / JS 的檔案，\
打包後的檔案，會產生在 `dist` 這個目錄裡，這包東西通常才是真正在部署環境上運行的東西。\
(我們的話會在 `frontend/dist` 這個目錄，下面會教你怎麼打包)

```
dist
├── favicon.ico
├── index.html
└── assets
    ├── chatroom.js
    ├── chatroom.css
    ├── all.css
    ├── index.js
    └── font.otf
```

### How

+ `npm run build`

  執行 `build` 指令後，所有前端程式碼，就會打包到 dist 目錄裡。

+ `npm run copy-resources`

  要執行 `copy-resources` 指令，是因為我們還有一些影片或者圖片資源放在前端。\
  所以打包完後，要複製進去。我使用 `robocopy`，這是 Windows 內建 CLI。\
  如果你是 Linux 平台，可能要去 `frontend/package.json` 那裡修改，改成使用其他複製工具。

#### Using `npm`
```
npm run build
```
```
npm run copy-resources
```

#### Using `pnpm`
```
pnpm build
```

```
pnpm copy-resources
```





## [⬆️][0] System Requirements Specification

### Functional Requirements

> 所有功能一併集中於 chat room

#### 翻譯模式 (Translation mode)
  - 🟢 翻譯功能
    - 使用者 (frontend) : 可上傳有卡片的圖片內容
    - 模型 (backend) : 回傳翻譯結果
  - 🟢 卡片顯示功能
    - 功能 (frontend) : 翻譯結果會以 [canvas 卡片][yugioh canvas card]呈現
  - 🟢 詳細資訊功能 
    - 功能 (backend) : 使用者給定密碼，並從 [ygoprodeck API] 中抓取資料更詳細資訊 (用於 [canvas 卡片][yugioh canvas card]呈現)
      - 比如卡面圖片、ATK、DEF、cardType、pendulumType 等等
#### 問答模式 (Q&A mode)
  - 🟢 問答功能
    - 使用者 (frontend) : 可輸入遊戲王相關提問內容
    - 模型 (backend) : 回傳解惑結果
  - 🟢 歷史紀錄功能
    - 使用者 (前端) : 可開啟很多 conversations，每個 conversation 有問答的 messages
  - ⚫ 登入功能
    - backend 需要實作比較多東西...
    - database: the schema of user, and conversation, account, password (記得 salting) ...
    - 登入 cookie ...

### Non Functional Requirements

> ...





## [⬆️][0] API

### Translate API
  ```ini
  [API]: /api/translate
  [HTTP Method]: POST
  [Request Headers]:
    {
      "Content-Type": "multipart/form-data",
    }
  [Request Parameters]:
    {
      "image": formData
    }
  [Response Headers]:
    {
      "Content-Type": "application/json",
    }
  [Response Body (Success)]:
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
  [Response Body (Failure)]:
    {
      "success": false,
      "errMessage": "(翻譯過程出錯)",
    }
  ```
### Question API
  ```ini
  [API]: /api/question
  [HTTP Method]: POST
  [Request Headers]:
    {
      "Content-Type": "text/plain",
    }
  [Request Body]:
    text
  [Response Headers]:
    {
      "Content-Type": "application/json",
    }
  [Response Body (Success)]:
    {
      "success": true,
      "answer": "(問答結果)",
    }
  [Response Body (Failure)]:
    {
      "success": false,
      "errMessage": "(問答過程出錯)",
    }
  ```

### Card Material API
  ```ini
  [API]: /api/assets/card-material
  [HTTP Method]: GET
  [Request URL]:
    Append the resource path to the URL. For example:
    /api/assets/card-material/yugioh/image/level.png
  [Response Headers]:
    {
      "Content-Type": "image/png",
    }
  [Response Body]:
    card material
  ```

### Card Image API
  ```ini
  [API]: /api/assets/card-image
  [HTTP Method]: GET
  [Request URL]:
    Append the card password to the URL. For example:
    /api/assets/card-image/14558127
  [Response Headers]:
    {
      "Content-Type": "image/jpeg",
    }
  [Response Body]:
    card image
  ```
