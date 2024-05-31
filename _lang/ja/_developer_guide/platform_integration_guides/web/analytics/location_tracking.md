---
nav_title: 位置情報の追跡
article_title: ウェブ上の位置追跡
platform: Web
page_order: 5
page_type: reference
description: "この記事では、Web で位置情報の追跡を有効にする方法について説明します。"
tool: Location

---

# 位置情報の追跡

> この記事では、Web で位置情報の追跡を有効にする方法について説明します。

ユーザーの現在地を設定するには、 [`getCurrentPosition()`][0] ジオロケーション API のメソッドを使用して、位置データを Braze に記録します。

\`\`\`javascript
import * as braze from "@braze/web-sdk";
function success(position) {
  var 座標 = position.座標;
  braze.getUser().setLastKnownLocation(
    座標、緯度、
    座標.経度、
    座標精度、
    座標、高度、
    座標高度精度
  );
()

navigator.geolocation.getCurrentPosition(success);
\`\`\`

通話 `navigator.geolocation.getCurrentPosition()` ユーザーがすでに許可または拒否していない限り、直ちにユーザーに許可を要求します。ユーザーの最後の既知の場所を設定する方法については、[JSDocs を][1] 参照してください。

## 単一の場所の記録

Web SDK が Braze サーバーにデータを送信すると、アプリケーションによって手動で設定されていない場合、ユーザーの国は IP アドレスから自動的に検出されます。

### 継続的な追跡

ページ読み込み中にユーザーの位置を継続的に追跡したい場合は、 [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)Geolocation API のメソッド。このメソッドは、ユーザーの位置が更新されるたびに成功コールバックを呼び出します。

\`\`\`javascript
function success(position) {
  var 座標 = position.座標;
  braze.getUser().setLastKnownLocation(
    座標、緯度、
    座標.経度、
    座標精度、
    座標、高度、
    座標高度精度
  );
()

navigator.geolocation.watchPosition(success);
\`\`\`

通話 `navigator.geolocation.watchPosition()` ユーザーがすでに許可または拒否していない限り、直ちにユーザーに許可を要求します。位置追跡の設定と停止については [、Mozilla 開発者ドキュメント][2] を参照してください。

[0]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
[1]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation
[2]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition
