---
nav_title: RudderStack
article_title:RudderStack
description:"この記事では、Brazeと、Android、iOS、WebアプリケーションにBrazeのシームレスな統合を提供するオープンソースの顧客データインフラであるRudderStackとのパートナーシップについて概説する。RudderStackを使えば、アプリ内の顧客イベントデータを直接Brazeに送信し、文脈に応じた状況分析を行うことができる"
page_type: partner
search_tag:Partner

---

# RudderStack

> \[RudderStack][1] は、顧客イベントデータを収集し、好みのデータウェアハウスやBrazeなどの数多くの分析プロバイダーにルーティングするためのオープンソースの顧客データインフラである。エンタープライズ対応で、イベントデータをその場で処理するための堅牢な変換フレームワークを提供する。

BrazeとRudderStackの統合は、Android、iOS、WebアプリケーションのためのネイティブSDK統合と、バックエンドサービスからのサーバー間統合を提供する。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| RudderStackアカウント | このパートナーシップを利用するには、[RudderStackアカウントが](https://app.rudderstack.com/)必要である。 |
| 設定されたソース | ソース][3] は、基本的に、Webサイト、モバイルアプリ、バックエンドサーバーなど、RudderStackに送信されるあらゆるデータの内部ソースである。Rudderstackで送信先としてBrazeを設定する前に、送信元を設定する必要がある。 |
| Braze REST API キー | `users.track` 、`users.identify` 、`users.delete` 、`users.alias.new` の権限を持つREST APIキー。<br><br>これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Brazeアプリキー | ダッシュボードでアプリキーを取得するには、**設定** **>アプリ設定** **>識別と**進み、アプリ名を見つける。関連する識別子文字列を保存する。
| データセンター | データセンターはBrazeダッシュボード\[インスタンス][15] 。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:ソースを追加する

Brazeへのデータ送信を開始するには、まずRudderStackアプリにデータソースが設定されていることを確認する必要がある。データソースの設定方法については、\[RudderStack][22] ] を参照のこと。

### ステップ2:送信先を設定する

データソースが設定されたので、RudderStackダッシュボードで、**Destinationsの**下にある**ADD DESTINATIONを**選択する。利用可能な送信先のリストから**Brazeを**選択し、**Nextを**クリックする。

Braze送信先で、アプリキー、Braze REST APIキー、データクラスタ、およびネイティブSDKオプション（デバイスモードのみ）を指定する。ネイティブSDKオプションをオンにすると、BrazeネイティブSDKを使用してイベントを送信する。 

![][0]{: style="max-width:70%;margin-bottom:15px;border:none;"}

### ステップ3:統合のタイプを選ぶ

RudderStackのWebおよびネイティブクライアントサイドライブラリーをBrazeと統合するには、以下のいずれかの方法を選択する：

- [サイド・バイ・サイド/デバイス・モード](#device-mode)**:**RudderStackは、クライアント（ブラウザまたはモバイルアプリケーション）から直接Brazeにイベントデータを送信する。
- [サーバー間/クラウドモード](#cloud-mode)**:**Braze SDKはイベントデータを直接Rudderstackに送り、それを変換してBrazeにルーティングする。
- [ハイブリッドモード](#hybrid-mode)**:**ハイブリッドモードを使用して、iOSとAndroidの自動生成イベントとユーザー生成イベントを、単一の接続を使用してBrazeに送信する。

{% alert note %}
RudderStackの[接続モードと](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/)それぞれの利点について学習する。
{% endalert %}

#### サイド・バイ・サイドの統合（デバイス・モード） {#device-mode}

このモードでは、Webサイトやモバイルアプリに設定したBraze SDKを使用して、イベントをBrazeに送信できる。

BrazeのGitHubリポジトリで、[サポートされる方法の](#supported-methods)説明に従って、プラットフォーム用のRudderStack SDKへのマッピングを設定する：

- \[Android]\[アンドロイド］
- \[iOS]\[アイオス］
- \[SWIFT]\[スイフト]。
- \[Web]\[ウェブ]。
- \[リアクト・ネイティブ]\[リアクト]。
- \[Flutter]\[フラッター]。

デバイスモードの統合を完了するには、[プロジェクトにBrazeを](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration)追加するためのRudderStackの詳しい説明を参照する。

#### サーバー間統合（クラウドモード） {#cloud-mode}

このモードでは、SDKはイベントデータをRudderstackサーバーに直接送信する。RudderStackはこのデータを変換し、目的の送信先にルーティングする。この変換は、RudderStackのtransformerモジュールを使って、RudderStackのバックエンドで行われる。

統合をイネーブルメントにするには、[サポートされるメソッドで](#supported-methods)説明されているように、RudderStackのメソッドをBrazeにマッピングする必要がある。

{% alert note %}
RudderStackのサーバーサイドSDK（Java、Python、Node.js、Go、Ruby）は、クラウドモードのみをサポートしている。これは、サーバー側のSDKがRudderstackバックエンドで動作し、Braze固有のSDKを読み込むことができないためだ。
{% endalert %}

{% alert important %}
サーバー間統合は、プッシュ通知やアプリ内メッセージングなどのBraze UI機能をサポートしていない。しかし、これらの機能は、デバイスモードの統合によってサポートされる。
{% endalert %}

#### ハイブリッド・モード {#hybrid-mode}

ハイブリッドモードを使用して、iOSとAndroidのソースからBrazeにすべてのイベントを送信する。 

Brazeにイベントを送信するためにハイブリッドモードを選択すると、Rudderstackは、イベントを送信する：
1. Braze SDKを初期化する。
2. ユーザーが作成したすべてのイベント（識別子、トラック、ページ、スクリーン、グループ）をクラウドモードでのみBrazeに送信し、デバイスモードからの送信をブロックする。
3. 自動生成イベント（アプリ内メッセージ、Braze SDKを必要とするプッシュ通知）をデバイスモード経由で送信する。

[ハイブリッドモードでイベントを送信](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode)するには、送信元と送信先を接続する際にハイブリッドモードオプションを使用する。次に、Brazeインテグレーションをプロジェクトに追加する。

## ステップ 4:追加設定を行う

初期設定完了後、Brazeでデータを正しく受信するために以下の設定を行う：

- **グループ通話でサブスクリプショングループを有効に**する：グループイベントでサブスクリプショングループのステータスを送信するには、この設定をイネーブルメントにする。詳しくは[グループを](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group)参照のこと。
- **カスタム属性を使用**する：Brazeの[階層化カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)機能を使用してセグメントを作成し、カスタム属性オブジェクトを使用してメッセージをパーソナライズする場合は、この設定をイネーブルにする。詳細については、[階層化されたカスタム属性としてユーザー特性を送信](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes)するを参照のこと。
- **匿名ユーザーのイベントをトラッキング**、追跡する：この設定をイネーブルにすると、匿名のユーザーアクティビティをトラッキングし、その情報をBrazeに送信する。

### デバイスモード設定

以下の設定は、[デバイスモード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode)経由でBrazeにイベントを送信する場合にのみ適用される：

- **クライアント側のイベントフィルター**：この設定により、Brazeに流すイベントをブロックするか許可するかを指定できる。この設定の詳細については、[クライアント側のイベント](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/)フィルターを参照のこと。
- **形質を重複させない**：この設定をイネーブルメントにすると、コールのユーザートラ イツが重複排除される。 [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify)を呼び出す。
- **Brazeのログを表示**する：この設定は、[JavaScript SDKを](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/)ソースとして使用する場合にのみ適用される。ユーザーにBrazeのログを表示するには、イネーブルメントを有効にする。
- **OneTrustのCookieカテゴリー**：この設定により、[OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/)Cookie同意グループをBrazeに関連付けることができる。

## サポートされている方法

Brazeは、RudderStackメソッドのidentify、track、screen、page、group、aliasをサポートしている。

{% tabs %}
{% tab Identify %}

RudderStack[`identify` メソッドは](https://rudderstack.com/docs/destinations/marketing/braze/#identify)、ユーザーとそのアクションを関連付ける。RudderStackは、一意のユーザーIDと、名前、メール、IPアドレスなど、そのユーザーに関連するオプションの特徴をキャプチャする。

**識別子コールのデルタマネージャー**<br>
デバイスモード経由でBrazeにイベントを送信する場合、`identify` コールを重複排除することでコストを節約できる。そのためには、ダッシュボードのDeduplicate Traits設定をイネーブルメントにする。そしてRudderStackは、変更または修正された属性（trait）のみをBrazeに送信する。

**ユーザーを削除する**<br>
RudderStack[Data Regulation APIの](https://www.rudderstack.com/docs/api/data-regulation-api/) [Suppression with Deleteレギュレーションを](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation)使用して、Brazeでユーザーを削除することができる。

{% endtab %}
{% tab Track %}

RudderStackの[`track` メソッドは](https://rudderstack.com/docs/destinations/marketing/braze/#track)、すべてのユーザーのアクティビティと、それらのアクティビティに関連するプロパティをキャプチャする。

**注文完了**<br>
RudderStack Ecommerce API][20] を使用して、`Order Completed` という名前のイベントの track メソッドを呼び出すと、RudderStack はそのイベントにリストされている商品を [`purchases`][21] として Braze に送信する。

{% endtab %}
{% tab Screen %}

RudderStackの[`screen` メソッドでは](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen)、ユーザーのモバイル画面表示を、表示画面に関する追加情報とともに記録することができる。

{% endtab %}
{% tab Page %}

RudderStackの[`page` ](https://rudderstack.com/docs/destinations/marketing/braze/#page)、Webサイトのページビューを記録することができる。また、そのページに関するその他の関連情報もキャプチャする。

{% endtab %}
{% tab Group %}

RudderStackの[`group` メソッドでは](https://rudderstack.com/docs/destinations/marketing/braze/#group)、ユーザーをグループに関連付けることができる。

**サブスクリプショングループのステータス**<br>
サブスクリプショングループのステータスを更新するには、RudderStackダッシュボードの "Enable subscription groups in group call "設定をイネーブルにし、グループコールでサブスクリプショングループのステータスを送信する。

{% endtab %}
{% tab Alias %}

RudderStackの[`alias` メソッドでは](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias)、既知のユーザーの異なるIDをマージすることができる。RudderStackは、Brazeのエイリアス呼び出しをクラウドモードでのみサポートしていることに注意。

{% endtab %}
{% endtabs %}

## ユーザー特性を階層化カスタム属性として送信する

ユーザー特性を階層化カスタム属性としてBrazeに送信し、それに対して追加、更新、削除のオペレーションを実行することができる。そのためには、RudderStackでBraze送信先を設定する際に、"Use Custom Attributes Operation dashboard "の設定をイネーブルにする。この機能はクラウドモードでのみ利用できる。

`identify` 、階層化されたカスタム属性として、以下の形式でユーザーの特徴を送信することができる：
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Mike"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

`track` 、`page` 、`screen` コールを介してカスタムユーザー属性としてユーザーの特徴を送信するには、`traits` をイベントの文脈に応じたフィールドとして渡す：
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Mike"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
更新と削除の操作では、`identifier` が必須キーとなる。ネストされた配列にadd、update、removeオペレーションが存在しない場合、RudderStackはデフォルトでcreateオペレーションを使用してプロパティを作成する。階層化されたカスタム属性の送信については、「[オブジェクトの配列]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)」を参照のこと。
{% endalert %}

[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}
[1]: https://rudderstack.com/
[3]: https://www.rudderstack.com/docs/dashboard-guides/sources/
[15]: {{site.baseurl}}/api/basics/#endpoints
[20]: https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/
[21]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]: https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started
\[アンドロイド）： https://github.com/rudderlabs/rudder-integration-braze-android
\[ios]である： https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master
\[SWIFT]である： https://github.com/rudderlabs/rudder-integration-braze-swift
\[Web]： https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze
\[反応する）： https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native
\[フラッター]： https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter