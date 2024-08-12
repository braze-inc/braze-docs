---
nav_title: リンクを新しいタブで開く
article_title: アプリ内メッセージリンクをウェブの新しいタブで開く
platform: Web
channel: in-app messages
page_order: 8
page_type: reference
description: "この記事では、Web アプリケーションの新しいタブで開くようにアプリ内メッセージ リンクを設定する方法について説明します。"

---

# リンクを新しいタブで開く

> この記事では、Web アプリケーションの新しいタブで開くようにアプリ内メッセージ リンクを設定する方法について説明します。

アプリ内メッセージリンクを新しいタブで開くように設定するには、 `openInAppMessagesInNewTab` オプション `true` アプリ内メッセージのクリックからのすべてのリンクを新しいタブまたはウィンドウで強制的に開きます。

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
