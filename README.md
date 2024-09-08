# paper-translate-bot

arXiv のリンクが送られた論文の TL;DR と abstract を Semantic Scholor から取得して DeepL で翻訳した結果を返す bot

## 環境構築

uv を使用

```bash
$ uv sync
```

## 設定事項

`.env`に以下を追加

```
SLACK_APP_TOKEN_PAPER='SlackのAppのAPIトークン (xapp-から始まる)'
SLACK_BOT_TOKEN_PAPER='SlackのBotのAPIトークン (xoxb-から始まる)'
DEEPL_API_KEY='DeepLのAPIキー'
```

### Slack API

#### App の token

`Basic Information -> App-Level Tokens -> Generate Token and Scopes`で生成

- Scope は`connections:write`
- Socket Mode を有効化しておく
- Event Subscriptions から Events を有効化
  - `message.channels` イベントを指定

#### Bot Token Scopes

`Features -> OAuth & Permissions -> Scopes`

```
channels:history
channels:read
chat:write
im:history
im:read
im:write
users:read
```

## 参考

### Slack API

https://zenn.dev/kou_pg_0131/articles/slack-api-post-message
https://zenn.dev/t_yng/scraps/8374a9616c235e
https://qiita.com/seratch/items/1a460c08c3e245b56441
https://slack.dev/python-slack-sdk/web
https://slack.dev/bolt-python/ja-jp/

### Semantic Scholor

https://api.semanticscholar.org/api-docs/#tag/Paper-Data
