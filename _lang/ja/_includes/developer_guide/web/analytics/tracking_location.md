## 現在地を記録する

ユーザーの現在地を取得するには、ジオロケーションAPIの [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition)メソッドを使う。これにより、ユーザーはトラッキングを許可するかしないかを即座に選択することになる（すでに許可している場合を除く）。

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

Brazeにデータが送信される際、SDKはユーザーのIPアドレスから自動的にユーザーの国を検出できるようになった。詳細については、[setLastKnownLocation() を](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation)参照のこと。

## 位置情報の追跡を続ける

ページが読み込まれている間、ユーザーの位置情報の追跡を継続的に行うには、geolocation APIの [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)メソッドを使う。このメソッドをトラッキング, 追跡すると、ユーザーにトラッキングの許可または不許可を即座に促す（すでに許可している場合を除く）。

もし彼らがオプトインすれば、位置情報が更新されるたびに成功コールバックが呼び出されるようになる。

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

{% alert important %}
トラッキング追跡を無効にする方法については、[Mozilla開発者向けドキュメントを](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)参照のこと。
{% endalert %}
