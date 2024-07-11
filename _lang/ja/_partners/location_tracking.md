---
nav_title: 位置追跡
article_title:Web の位置追跡
platform:Web
page_order:5
page_type: reference
description:「この記事では、Webの位置追跡を有効にする方法について説明します。」
tool:ロケーション

---

# 位置情報の追跡

> この記事では、Web の位置追跡を有効にする方法について説明します。

ユーザーの現在地を設定するには、 [`getCurrentPosition()`][0] メソッドを呼び出し、位置情報をBrazeに記録します。

```javascript
import * as braze from "@braze/web-sdk";
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.getCurrentPosition(success);
```

天職 `navigator.geolocation.getCurrentPosition()` は、ユーザーがすでに権限を付与または拒否していない限り、ユーザーに直ちに許可を要求します。を参照してください。 [JSドックス][1] ユーザーの最新の既知の場所の設定については、こちらをご覧ください。

## 1 つの場所のログ記録

Web SDKがBrazeサーバーにデータを送信すると、アプリケーションによって手動で設定されていない場合、ユーザーの国はIPアドレスから自動的に検出されます。

### 継続的な追跡

ページの読み込み中にユーザーの位置情報を継続的に追跡する場合は、 [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) メソッドを使用します。このメソッドは、ユーザーの位置情報が更新されるたびに成功コールバックを呼び出します。

```javascript
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.watchPosition(success);
```

天職 `navigator.geolocation.watchPosition()` は、ユーザーがすでに権限を付与または拒否していない限り、ユーザーに直ちに許可を要求します。を参照してください。 [Mozilla 開発者向けドキュメント][2] 位置追跡の構成と停止については、を参照してください。

[0]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
[1]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation
[2]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition
