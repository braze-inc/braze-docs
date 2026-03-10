{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 最後の既知の位置を設定する

ユーザーの手動で最後の既知の位置を設定するには、メソッド`setLastKnownLocation`を使用する。Braze SDK以外で位置情報を収集する場合に役立つ。

```javascript
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);
```

- Androidでは、`latitude`と`longitude`が必須だ。`altitude`、`horizontalAccuracy`、およびは任意`verticalAccuracy`だ。
- iOSでは、`latitude`、および`horizontalAccuracy``longitude`が必須である。`altitude`とは任意`verticalAccuracy`である。

クロスプラットフォーム互換性のため、最低限、`longitude```、``、および`horizontalAccuracy`\`\`を提供すること`latitude`。

## カスタム位置属性の設定

ユーザープロファイルにカスタム属性を設定するには、メソッド`setLocationCustomAttribute`を使用する。

```javascript
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);
```

## 位置情報の初期化を要求する（Androidのみ）

ユーザーが位置情報の権限を与えた後、AndroidでBrazeの位置`requestLocationInitialization`情報機能を初期化するために呼び出す。この方法はiOSではサポートされておらず、iOSのジオフェンスや位置情報機能には必要ない。

```javascript
Braze.requestLocationInitialization();
```

## ジオフェンス

ジオフェンスはiOSとAndroidの両方でサポートされている。デフォルトでは、Braze SDKは位置情報が利用可能な場合、自動的にジオフェンスをリクエストし監視する。ほとんどの統合では、この自動設定を頼りにできる。

### ジオフェンスの手動リクエスト

特定のGPS座標に対してジオフェンスの更新を手動で要求するには、を使用する`requestGeofences`。これはiOSとAndroidの両方で利用可能だ。この方法を使う場合、ネイティブ設定で自動ジオフェンスリクエストを無効にせよ。そうすればSDKが手動リクエストを上書きしない。

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
