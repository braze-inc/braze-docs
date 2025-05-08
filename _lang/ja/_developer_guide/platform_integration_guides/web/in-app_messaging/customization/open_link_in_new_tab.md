---
nav_title: 新規タブでリンクを開く
article_title: Web の新規タブでアプリ内メッセージリンクを開く
platform: Web
channel: in-app messages
page_order: 8
page_type: reference
description: "ここでは、ウェブアプリ用の新しいタブで開封へのアプリ内メッセージリンクを設定する方法について説明します。"

---

# 新しいタブでリンクを開く

> ここでは、ウェブアプリ用の新しいタブで開封へのアプリ内メッセージリンクを設定する方法について説明します。

新しいタブでアプリ内メッセージのリンクが開くように設定するには、`openInAppMessagesInNewTab` オプションを `true` に設定して、アプリ内メッセージでのクリックによるすべてのリンク先が新しいタブまたはウィンドウで開くように強制します。

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
