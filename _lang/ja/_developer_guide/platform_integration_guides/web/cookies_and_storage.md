---
nav_title: クッキーと保存
article_title: ウェブ用クッキーとストレージ
platform: Web
page_order: 15
page_type: reference
description: "この参考記事では、Braze Web SDKで使用されるさまざまなクッキーについて説明する。"

---

# クッキーと保存

> この記事では、Braze Web SDKが使用するさまざまなクッキーについて説明する。

読み進める前に、Braze Web SDKは、ウェブサイトがSDKを[初期化](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)するまで、ブラウザにデータを保存しない（クッキーなど）ことに注意すること。

さらに、これらの値は変更される可能性があり、統合を通じて直接アクセスすべきではありません。代わりに、パブリックAPIインターフェースについては、[JavaScriptのドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)参照のこと。

{% multi_lang_include archive/web-v4-rename.md %}

## クッキー {#cookies}

このセクションでは、Braze Web SDKにおけるCookieの設定および管理方法について説明する。Braze Web SDK は、最大限の柔軟性、法令遵守、メッセージングの関連性を提供するように構築されています。

Braze がCookie を作成すると、新しいセッションで自動的に更新される400 日の有効期限で保存されます。

### Cookie を無効にする {#disable-cookies}

すべての Cookie を無効にするには、Web SDK を初期化する際に [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) オプションを使用します。
Cookie を無効にすると、サブドメイン間を移動する匿名ユーザーを関連付けることができなくなり、各サブドメインで新しいユーザーが発生します。

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Brazeのトラッキング全般を停止したり、保存されたブラウザデータをすべて消去するには [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK)および [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata)SDKメソッドを参照のこと。これらの2つのメソッドは、ユーザーが同意を取り消した場合、または SDK の初期化後に Braze のすべての機能を停止する場合に役立ちます。

### クッキー一覧

|クッキー|説明|サイズ|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|現在ログインしているユーザーが変更されたかどうかを判断し、イベントを現在のユーザーに関連付けるために使用される。|`changeUser` に渡された値のサイズに基づく|
|`ab.storage.sessionId.[your-api-key]`|メッセージを同期し、セッション分析を計算するために、ユーザーが新しいセッションを開始しているか、既存のセッションを開始しているかを判断するために使用されるランダムに生成される文字列。|~200バイト|
|`ab.storage.deviceId.[your-api-key]`|匿名ユーザーを識別し、ユーザーのデバイスを区別し、デバイスベースのメッセージングを可能にするために使用されるランダムに生成される文字列。|~200バイト|
|`ab.optOut`|`disableSDK` が呼び出されたときにユーザーのオプアウト設定を格納するために使用されます|~40バイト|
|`ab._gd`|ルートレベルの Cookie ドメインを決定するために一時的に作成 (その後削除) されます。これにより、サブドメイン間で SDK が適切に動作できるようになります。|該当なし|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## デバイスのプロパティ

デフォルトでは、Brazeは以下のデバイスレベルのプロパティを収集し、デバイス、言語、タイムゾーンに基づくメッセージのパーソナライズを可能にする：

* ブラウザ
* BROWSER_VERSION
* 言語
* OS
* RESOLUTION
* TIME_ZONE
* USER_AGENT

`devicePropertyAllowlist` 初期化オプションを[`DeviceProperties`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html) のリストに設定することで、収集するプロパティを無効にしたり指定したりできます。 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

デフォルトでは、すべてのフィールドが有効になっています。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。

自動的に収集されるデバイスプロパティの詳細については、[SDK データ収集オプション]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)をご覧ください。 


