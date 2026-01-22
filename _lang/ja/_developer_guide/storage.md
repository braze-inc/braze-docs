---
nav_title: ストレージ
article_title: iOS 用ストレージ
page_order: 3.60
page_type: reference
description: "Braze SDKによって保存されるさまざまなデバイスレベルプロパティについて学習する。"
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# ストレージ

> Braze SDKによって保存されるさまざまなデバイスレベルプロパティについて学習する。

## デバイスのプロパティ

デフォルトでは、Braze は以下のデバイスレベルプロパティを収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

{% tabs %}
{% tab web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}

{% tab android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` と `TIMEZONE` は `null` または空白の場合は収集されません。`GOOGLE_ADVERTISING_ID` は SDK によって自動的に収集されないため、[`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) 経由で渡す必要があります。
{% endalert %}
{% endtab %}

{% tab swift %}
- デバイスの通信事業者 ([`CTCarrier` 非推奨](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier)に関する注記を参照)
- デバイスのロケール
- デバイスモデル
- デバイス OS のバージョン
- プッシュ認証ステータス
- プッシュ表示オプション
- プッシュ通知が有効
- デバイスの解像度
- デバイスのタイムゾーン

{% alert note %}
Braze SDK はIDFA を自動的に収集しません。アプリはオプションで、以下のメソッドを直接実装することで IDFA を Braze に渡すことができます。アプリは IDFA を Braze に渡す前に、アプリトラッキングの透明性フレームワークを通じてエンドユーザーによるトラッキングへの明示的なオプトインを取得する必要があります。

1. 広告のトラッキング状態を設定するには [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/) を使用します。
2. 広告主の識別子 (IDFA) を設定するには、[`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/) を使用します。
{% endalert %}
{% endtab %}
{% endtabs %}

デフォルトでは、すべてのプロパティが有効になっています。しかし、手動で有効にも無効にもできます。Braze SDKの機能の中には、特定のプロパティ（ローカルタイムゾーン配信やタイムゾーンなど）を必要とするものがあるため、本番環境にリリースする前に、必ず設定をテストしておくことに留意すること。

{% tabs %}
{% tab web %}
例えば、許可リストに登録するデバイスの言語を指定することができます。詳細については、[`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) の`devicePropertyAllowlist` オプションを参照してください。

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}

{% tab android %}
たとえば、許可リストに登録する Android OS バージョンとデバイスロケールを指定できます。詳細は [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html)と [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html)メソッドを参照のこと。 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
たとえば、許可リストに登録するタイムゾーンとロケール収集を指定できます。詳細については、`configuration` オブジェクトの [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) プロパティを参照してください。

{% subtabs %}
{% subtab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert tip %}
自動的に収集されるデバイスプロパティの詳細については、[SDKデータ収集を]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)参照のこと。
{% endalert %}

## Cookie を保存する (Web のみ) {#cookies}

[ Web Braze SDK を初期化](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)すると、有効期限 400 日の Cookie が作成および保存され、新しいセッションで自動的に更新されます。

以下の Cookie が保存されます。

|クッキー|説明|サイズ|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|現在ログインしているユーザーが変更されたかどうかを判断し、イベントを現在のユーザーに関連付けるために使用される。|`changeUser` に渡された値のサイズに基づく|
|`ab.storage.sessionId.[your-api-key]`|メッセージを同期し、セッション分析を計算するために、ユーザーが新しいセッションを開始しているか、既存のセッションを開始しているかを判断するために使用されるランダムに生成される文字列。|~200バイト|
|`ab.storage.deviceId.[your-api-key]`|匿名ユーザーを識別し、ユーザーのデバイスを区別し、デバイスベースのメッセージングを可能にするために使用されるランダムに生成される文字列。|~200バイト|
|`ab.optOut`|`disableSDK` が呼び出されたときにユーザーのオプアウト設定を格納するために使用されます|~40バイト|
|`ab._gd`|ルートレベルの Cookie ドメインを決定するために一時的に作成 (その後削除) されます。これにより、サブドメイン間で SDK が適切に動作できるようになります。|該当なし|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Cookie を無効にする {#disable-cookies}

すべての Cookie を無効にするには、Web SDK を初期化する際に [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) オプションを使用します。これにより、サブドメインをまたいで移動する匿名ユーザーを関連付けることができなくなり、各サブドメインで新しいユーザーが発生することになる。

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Brazeのトラッキング全般を停止したり、保存されたブラウザデータをすべて消去するには [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK)および [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata)SDKメソッドを参照のこと。これらの2つのメソッドは、ユーザーが同意を取り消した場合、または SDK の初期化後に Braze のすべての機能を停止する場合に役立ちます。
