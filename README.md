# example-websocket
Example project of websocket app

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

# CREDIT

This is a practice for websocket in python.
The contents are based on https://websockets.readthedocs.io/en/stable/intro/tutorial1.html
