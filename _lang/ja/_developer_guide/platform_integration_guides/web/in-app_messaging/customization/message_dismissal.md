---
nav_title: メッセージ却下
article_title: Webのアプリ内解雇
platform: Web
channel: in-app messages
page_order: 2
page_type: reference
description: "この記事では、ウェブアプリライケーションのアプリ内メッセージ解雇について説明します。"

---

# メッセージ却下

> この記事では、ウェブアプリライケーションのアプリ内メッセージ解雇の処理方法について説明します。

デフォルトでは、アプリ内メッセージが表示されているときにエスケープボタンを押すか、ページのグレー表示されているバックグラウンドをクリックすると、メッセージが消えます。`requireExplicitInAppMessageDismissal` [初期化オプション][41]を`true`に設定して、この動作を防ぎ、メッセージを消去するために明示的なボタンをクリックする必要があります。 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions
