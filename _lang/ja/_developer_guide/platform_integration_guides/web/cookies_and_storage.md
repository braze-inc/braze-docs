---
nav_title: クッキーと保存
article_title: ウェブ用クッキーとストレージ
platform: Web
page_order: 15
page_type: reference
description: "この参考記事では、Braze Web SDKで使用されるさまざまなCookieについて説明します。"

---

# クッキーと保存

> この記事では、Braze Web SDKが使用するさまざまなCookieについて説明します。

読み進める前に、Braze Web SDKは、ウェブサイトがSDKを[初期化][5]するまで、ブラウザにデータを保存しないことに注意してください（クッキーなど）。

また、これらの値は変更される可能性があるため、統合を通じて直接アクセスするべきではありません。代わりに、公開APIインターフェースについては、[JavaScriptのドキュメントを][1]参照してください。

{% multi_lang_include archive/web-v4-rename.md %}

## クッキー {#cookies}

このセクションでは、Braze Web SDKにおけるCookieの設定および管理方法について説明します。Braze Web SDKは、最大限の柔軟性、法令遵守、メッセージング関連性を提供するように構築されています。

BrazeがCookieを作成する場合、Cookieは1年間の有効期限で保存され、新しいセッションで自動的に更新されます。

### クッキーを無効にする {#disable-cookies}

すべてのクッキーを無効にするには、Web SDKの初期化時に [`noCookies`][6]オプションを使用してください。
クッキーを無効にすると、サブドメイン間を移動する匿名ユーザーを関連付けることができなくなり、各サブドメインで新しいユーザーが発生します。

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Brazeのトラッキング全般を停止したり、保存されたブラウザデータをすべて消去するには [`disableSDK`][3]および [`wipeData`][4]SDKメソッドを参照してください。これらの2つのメソッドは、ユーザーが同意を取り消した場合、またはSDKがすでに初期化された後にBrazeのすべての機能を停止したい場合に便利です。

### クッキー一覧

|クッキー|説明|サイズ
|---|----|---|---|
|`ab.storage.userId.[your-api-key]` ｜現在ログインしているユーザーが変更されたかどうかを判断し、イベントを現在のユーザーに関連付けるために使用される。｜`changeUser` ｜に渡される値のサイズに基づく。
|`ab.storage.sessionId.[your-api-key]`|メッセージを同期し、セッション分析を計算するために、ユーザーが新しいセッションを開始しているか、既存のセッションを開始しているかを判断するために使用されるランダムに生成される文字列。
|`ab.storage.deviceId.[your-api-key]` ｜匿名ユーザーを識別し、ユーザーのデバイスを区別し、デバイスベースのメッセージングを可能にするために使用されるランダムに生成される文字列。
|`ab.optOut`|`disableSDK` が呼び出されたときに、ユーザーのオプトアウト・プリファレンスを保存するために使用される|~40バイト|。
|`ab._gd`|ルートレベルのクッキー・ドメインを決定するために一時的に作成され（その後削除され）、SDKがサブドメイン間で適切に動作するようにします。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## デバイスのプロパティ

デフォルトでは、Braze は以下のデバイスレベルプロパティを収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

* ブラウザー
* ブラウザーのバージョン
* 言語 
* OS
* 解像度
* タイムゾーン
* USER-AGENT:

`devicePropertyAllowlist` 初期化オプションを以下のリストに設定することで、収集したいプロパティを無効にしたり、指定したりすることができる。 [`DeviceProperties`][2]. 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

デフォルトでは、すべてのフィールドが有効になっています。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。

自動的に収集されるデバイス・プロパティの詳細については、[SDKデータ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)オプションをご覧ください。 


[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html
[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK
[4]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata
[5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[6]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions
