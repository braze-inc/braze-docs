---
nav_title: LLMで構築する
article_title: LLMを用いた構築
page_order: 4
description: "Brazeのドキュメントを使ってAIコーディングアシスタントの使い方を学習し、SDK統合のワークフローを加速させる方法を知ろう。"
platform:
  - Web
  - React Native
---

# LLMを用いた構築

> AIコードアシスタントを使って、Brazeの統合ワークフローを加速させる。Context7を介してIDEをBraze Docs MCPサーバーに接続し、開発環境内で正確かつ最新のSDKガイダンスを直接入手できる。

AIコーディングアシスタントは、統合コードの記述や問題のトラブルシューティング、Braze SDK機能の探索を支援できる。ただし、適切なコンテキストが与えられている場合に限る。Braze Docs MCPサーバーは、AIアシスタントにBrazeのドキュメントへ直接アクセスする権限を与える。これにより、最新のSDKリファレンスに基づいて正確なコードスニペットを生成し、技術的な質問に答えることができる。

## Braze Docs MCPへの接続

[Context7は、](https://context7.com/braze-inc/braze-docs)AIアシスタントとBrazeのドキュメントライブラリーをつなぐ橋渡し役だ。IDEのMCP設定にContext7を追加すれば、AIアシスタントがBrazeの全ドキュメントセットを照会し、必要なSDKリファレンス、コード例、統合ガイドをオンデマンドサービスで取得できる。

### コンテキスト7の設定

Context7を通じてAIアシスタントをBraze Docs MCPに接続するには、IDEの\`.env`mcp.json``ファイルに以下の設定を追加する。

{% tabs %}
{% tab Cursor %}
[カーソル](https://cursor.com/)で、**設定**＞**ツールと統合**＞**MCPツール**＞**カスタムMCPを追加**へ移動し、以下のスニペットを追加する：

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

設定を保存し、Cursorを再起動する。AIアシスタントは、プロンプトにを含める`use context7`ことで、Context7経由でBrazeのドキュメントにアクセスできるようになった。
{% endtab %}

{% tab Claude %}
Claude Desktopで、**設定**＞**開発者**＞**設定編集**へ移動し、設定`claude_desktop_config.json`ファイルに以下を追加する：

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

設定を保存し、Claude Desktopを再起動する。
{% endtab %}

{% tab VS Code %}
以下の内容を VS Code の  `settings.json`または`.vscode/mcp.json`  ファイルに追加する：

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

設定を保存し、VS Codeを再起動する。
{% endtab %}
{% endtabs %}

{% alert note %}
Context7は[Braze MCPサーバー]({{site.baseurl}}/developer_guide/mcp_server/)とは異なる。Context7はAIアシスタントに**Brazeのドキュメント**へのアクセス権を提供する。一方、Braze MCPサーバーは**Brazeワークスペースデータ**（キャンペーン、セグメント、分析など）への読み取り専用アクセス権を提供する。両方を一緒に使うことで、より完全なAI支援開発体験を得られる。
{% endalert %}

## Braze SDK開発者のためのライティングプロンプト

Context7を設定した後、プロンプトにを含める`use context7`ことで、AIアシスタントにBrazeのドキュメントをコンテキストとして参照するよう指示する。以下の例は、一般的なSDKタスクに対して効果的なプロンプトを書く方法を示す。

### React Native SDK

これらのプロンプトは[、Braze React Native SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/)の一般的な統合タスクを示している。

#### SDKの初期化

```text
Using the Braze React Native SDK, show me how to initialize the SDK 
in my App.tsx with an API key and custom endpoint. Include the 
configuration for automatic session tracking. Use context7.
```

#### プロパティ付きのカスタムイベントの記録

```text
I need to track user activity in my React Native app using the Braze 
React Native SDK. Show me how to log a custom event called 
"ProductViewed" with properties for product_id, category, and price. 
Use context7.
```

#### プッシュ通知の設定

```text
Using the Braze React Native SDK, walk me through requesting push 
notification permissions on both iOS and Android 13+. Include the 
code for registering the push token with Braze. Use context7.
```

#### アプリ内メッセージを処理する

```text
Show me how to subscribe to in-app messages using the Braze React 
Native SDK, including how to log impressions and button clicks 
programmatically. Use context7.
```

### ウェブSDK

これらのプロンプトは[、Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)の一般的な統合タスクを示している。

#### SDKの初期化

```text
Using the Braze Web SDK, show me how to initialize the SDK with 
braze.initialize(), including the API key, base URL, and options 
for enabling logging and automatic in-app message display. 
Use context7.
```

#### カスタムイベントと購入のトラッキング

```text
Using the Braze Web SDK, create a JavaScript module that logs a 
custom event called "VideoPlayed" with properties for video_id, 
duration_seconds, and completion_percentage. Also show how to log 
a purchase with product ID, price, currency code, and quantity. 
Use context7.
```

#### Web プッシュの登録

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to 
register a user for web push notifications after they click a 
"Subscribe to updates" button. Include the service worker setup. 
Use context7.
```

#### ユーザー属性の管理

```text
Using the Braze Web SDK, show me how to set standard user attributes 
(first name, email, country) and custom user attributes (favorite_genre, 
subscription_tier) for the current user. Use context7.
```

## プレーンテキストのドキュメント

Braze開発者ガイドのドキュメントは、AIツールや大規模言語モデル向けに最適化されたプレーンテキストファイルとしてアクセスできる。これらのファイルは、AIアシスタントがHTMLレンダリングのオーバーヘッドなしに解析・理解できる形式でBrazeのドキュメントを提供する。

| ファイル | 説明 |
|------|-------------|
| [llms.txt](https://www.braze.com/docs/developer_guide/llms.txt) | Braze開発者向けドキュメントページのタイトルと説明の索引だ。利用可能なドキュメントを見つけるための出発点としてこれを使え。 |
| [llms-full.txt](https://www.braze.com/docs/developer_guide/llms-full.txt) | Braze開発者向けドキュメントの完全版を、単一のプレーンテキストファイルにまとめたものだ。LLMが消費しやすい形式でフォーマットされている。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

これらのファイルは[標準llms.txt](https://llmstxt.org/)に従っている。これはAIツールがドキュメントにアクセスできるようにするための新たな慣例だ。これらのファイルはプロンプト内で直接参照できるし、内容をLLMに貼り付けて文脈として使える。
