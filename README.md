# example-websocket
Example project of websocket app

# 起動方法

`poetry shell`で仮想環境に入っておく。

## webサーバー

```shell
python -m http.server
```

## アプリサーバー

```shell
python app2.py
```

### watchする場合

```shell
watchmedo shell-command --patterns="*.py" --command='./run.sh'
```

watchmedoで`*.py`のファイル変更を検知できる

- 再起動する際に前のプロセスを殺してくれないので、run.shの中で殺している
- 初回に起動したときに自動で起動してくれないので、`touch *.py`などを実行して明示的にファイルを変更させる

# メモ

```javascript
  const websocket = new WebSocket("ws://localhost:8002");
  websocket.send("abcdef")
```

これは、エラーになる。

> uncaught DOMException: An attempt was made to use an object that is not, or is no longer, usable

```javascript
  const websocket = new WebSocket("ws://localhost:8002");
  setTimeout(() => {
    websocket.send("abcdef");
  }, 1000);
```

これは、OK

# メモ: connect4.jsのなかみ

- `createBoard(board)`で要素を作る
  - `board`は、`main2.js`から渡されるDOMのelement
    - `.board`で選択されている
  - `createBoard`の中で、`board`の子要素として`div.column`を7個作成
    - さらに、`div.column`の子要素として`div.cell`を6個作成
    - `columnElement.dataset.column = column;`で列番号を`div.column`elementの`dataset`に設定
      - https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset
      - HTML Elementに任意の名前で属性をくっつけれるらしい
  - これらの要素を格子状に並べるようにcssでコントロール

# CREDIT

This is a practice for websocket in python.
The contents are based on https://websockets.readthedocs.io/en/stable/intro/tutorial1.html
