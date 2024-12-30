## API Doc
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
    material of card
  ```

### Card Image API
  ```ini
  [API]: /api/assets/card-image
  [HTTP Method]: GET
  [Request URL]:
    Append the card code to the URL. For example:
    /api/assets/card-image/14558127
  [Response Headers]:
    {
      "Content-Type": "image/jpeg",
    }
  [Response Body]:
    image of card
  ```
