---
nav_title: キーと値のペア
article_title: Web用のアプリ内メッセージキーと値のペア
platform: Web
channel: in-app messages
page_order: 9
page_type: reference
description: "この記事では、アプリ内メッセージングのキーと値のペアを活用して、Webアプリケーションの情報を表示する方法について説明します。"

---

# キーと値のペア

> この記事では、アプリ内メッセージングのキーと値のペアを活用して、Webアプリケーションの情報を表示する方法について説明します。

アプリ内メッセージオブジェクトは、その`extras`プロパティとしてキーと値のペアを持つことがあります。これらは、アプリ内メッセージキャンペーンを作成する際に**設定**のダッシュボードで指定されます。これらは、アプリ内メッセージを使用してデータを送信し、サイトでさらに処理するために使用できます。以下に例を示します。

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
