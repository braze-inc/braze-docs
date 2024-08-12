---
nav_title: キーと値のペア
article_title: ウェブ向けアプリ内メッセージのキーと値のペア
platform: Web
channel: in-app messages
page_order: 9
page_type: reference
description: "この記事では、アプリ内メッセージングのキーと値のペアを活用して Web アプリケーションの情報を表示する方法について説明します。"

---

# キーと値のペア

> この記事では、アプリ内メッセージングのキーと値のペアを活用して Web アプリケーションの情報を表示する方法について説明します。

アプリ内メッセージオブジェクトは、キーと値のペアを `extras` 財産。これらは、アプリ内メッセージキャンペーンを作成するときに、ダッシュボードの [設定] で指定されます。これらを使用すると、アプリ内メッセージでデータを送信し、サイトでさらに処理することができます。以下に例を示します。

\`\`\`javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
// this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
  braze.showInAppMessage(inAppMessage) を返します。
    ()


  if (inAppMessage インスタンス braze.InAppMessage) {
const extras = inAppMessage.extras;
if (extras) {
for (const key in extras) {
console.log("key: " + key + ", value: " + extras[key]);
}
    ()
    ()
      braze.showInAppMessage(inAppMessage);
        });
      \`\`\`
