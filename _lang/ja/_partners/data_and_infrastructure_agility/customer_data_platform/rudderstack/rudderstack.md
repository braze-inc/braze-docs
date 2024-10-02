---
nav_title: RudderStack
article_title: RudderStack
description: "この記事では、Brazeと、Android、iOS、WebアプリケーションにBrazeのシームレスな統合を提供するオープンソースの顧客データ基盤であるRudderStackとのパートナーシップについて概説する。RudderStackを使えば、アプリ内の顧客イベントデータをBrazeに直接送信し、コンテキスト分析を行うことができる。"
page_type: partner
search_tag: Partner

---

# RudderStack

> \[RudderStack][1] は、顧客のイベントデータを収集し、好みのデータウェアハウスやBrazeのような数多くの分析プロバイダーにルーティングするためのオープンソースの顧客データ基盤である。エンタープライズ対応で、イベントデータをその場で処理するための堅牢な変換フレームワークを提供する。

BrazeとRudderStackの統合は、Android、iOS、WebアプリケーションのためのネイティブSDK統合と、バックエンドサービスからのサーバー間統合を提供する。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| RudderStackアカウント | このパートナーシップを利用するには、[RudderStackのアカウントが](https://app.rudderstack.com/)必要である。 |
| 設定されたソース | ソース][3] は基本的に、ウェブサイト、モバイルアプリ、バックエンドサーバーなど、RudderStackに送信されるあらゆるデータのオリジンである。RudderStackでBrazeをデスティネーションとして設定する前に、ソースを設定する必要がある。 |
| Braze REST API キー | `users.track` 、`users.identify` 、`users.delete` 、`users.alias.new` の権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Brazeアプリのキー | Brazeダッシュボードでアプリキーを取得するには、**「設定」**>「**アプリ設定**」>「**識別**」と進み、アプリ名を見つける。関連する識別子文字列を保存する。
| データセンター | データセンターはBrazeのダッシュボード\[instance][15].  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:ソースを追加する

Brazeへのデータ送信を開始するには、まずRudderStackアプリにソースが設定されていることを確認する必要がある。データソースの設定方法については、\[RudderStack][22] ] を参照のこと。

### ステップ2:目的地を設定する

データソースがセットアップされたので、RudderStackのダッシュボードで、**Destinationsの**下にある**ADD DESTINATIONを**選択する。利用可能な宛先リストから**Brazeを**選択し、**Nextを**クリックする。

Brazeデスティネーションで、アプリキー、Braze REST APIキー、データクラスタ、およびネイティブSDKオプション（デバイスモードのみ）を指定する。ネイティブSDKオプションをオンにすると、BrazeネイティブSDKを使用してイベントを送信する。 

![][0]{: style="max-width:70%;margin-bottom:15px;border:none;"}

### ステップ3:統合のタイプを選ぶ

RudderStackのWebおよびネイティブクライアントサイドライブラリをBrazeと統合するには、以下のいずれかの方法を選択する：

- [サイド・バイ・サイド/デバイス・モード](#device-mode)**:**RudderStackは、クライアント（ブラウザまたはモバイルアプリケーション）から直接Brazeにイベントデータを送信する。
- [サーバー間/クラウドモード](#cloud-mode)**:**Braze SDKはイベントデータを直接RudderStackに送り、それを変換してBrazeにルーティングする。
- [ハイブリッドモード](#hybrid-mode)**:**ハイブリッドモードを使用して、iOSとAndroidの自動生成イベントとユーザー生成イベントを、単一の接続を使用してBrazeに送信する。

{% alert note %}
RudderStackの[接続モードと](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/)それぞれの利点について詳しく知る。
{% endalert %}

#### サイド・バイ・サイドの統合（デバイス・モード） {#device-mode}

このモードでは、ウェブサイトまたはモバイルアプリに設定したBraze SDKを使用して、イベントをBrazeに送信できる。

BrazeのGitHubリポジトリで、[サポートされる方法の](#supported-methods)説明に従って、お使いのプラットフォーム用のRudderStack SDKへのマッピングを設定する：

- \[アンドロイド]\[アンドロイド]
- \[iOS]\[ios]
- \[スウィフト]\[スウィフト]
- \[Web]\[web]
- \[リアクト・ネイティブ]\[react]
- \[フラッター]\[flutter]

デバイスモードの統合を完了するには、[プロジェクトにBrazeを追加](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration)するためのRudderStackの詳しい説明を参照する。

#### サーバー間統合（クラウドモード） {#cloud-mode}

このモードでは、SDKはイベントデータを直接RudderStackサーバーに送信する。そして、RudderStackはこのデータを変換し、目的の目的地にルーティングする。この変換は、RudderStackのtransformerモジュールを使ってRudderStackのバックエンドで行われる。

統合を有効にするには、[サポートされるメソッドで](#supported-methods)説明されているように、RudderStackのメソッドをBrazeにマッピングする必要がある。

{% alert note %}
RudderStackのサーバーサイドSDK（Java、Python、Node.js 、Go、Ruby）は、クラウドモードのみをサポートしている。これは、サーバー側のSDKがRudderStackのバックエンドで動作し、ブレーズ固有のSDKをロードできないためだ。
{% endalert %}

{% alert important %}
サーバー間の統合は、プッシュ通知やアプリ内メッセージングなどのBraze UI機能をサポートしていない。しかし、これらの機能は、デバイスモードの統合によってサポートされる。
{% endalert %}

#### ハイブリッド・モード {#hybrid-mode}

ハイブリッドモードを使用して、iOSとAndroidのソースからすべてのイベントをBrazeに送信する。 

Brazeにイベントを送信するためにハイブリッドモードを選択した場合、RudderStack：
1. Braze SDKを初期化する。
2. ユーザーが生成したすべてのイベント（identify、track、page、screen、group）をクラウドモードからのみBrazeに送信し、デバイスモードからの送信をブロックする。
3. 自動生成イベント（アプリ内メッセージ、Braze SDKを必要とするプッシュ通知）をデバイスモード経由で送信する。

[ハイブリッドモードでイベントを送信](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode)するには、ソースをBrazeデスティネーションに接続する際にハイブリッドモードオプションを使用する。次に、Brazeインテグレーションをプロジェクトに追加する。

## ステップ4:追加設定を行う

初期設定完了後、Brazeでデータを正しく受信するために以下の設定を行う：

- **グループ通話でサブスクリプショングループを有効にする**：グループイベントで購読グループのステータスを送信するには、この設定を有効にする。詳しくは[グループを](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group)参照のこと。
- **カスタム属性を使用する**：Brazeの[ネストされたカスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)機能を使用してセグメントを作成し、カスタム属性オブジェクトを使用してメッセージをパーソナライズする場合は、この設定を有効にする。詳細については、[ネストされたカスタム属性としてユーザー特性を送信するを](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes)参照のこと。
- **匿名ユーザーのイベントを追跡**する：この設定を有効にすると、匿名のユーザーの活動が追跡され、その情報がBrazeに送信される。

### デバイスモード設定

以下の設定は、[デバイスモード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode)経由でBrazeにイベントを送信する場合にのみ適用される：

- **クライアント側のイベントフィルタリング**：この設定により、Brazeに流れるイベントをブロックするか、許可するかを指定できる。この設定の詳細については、[クライアント側イベントフィルタリングを](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/)参照のこと。
- **形質を重複させない**：この設定を有効にすると、コール内のユーザー形質が重複排除される。 [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify)を呼び出す。
- **Brazeのログを表示する**：この設定は、[JavaScript SDKを](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/)ソースとして使用する場合にのみ適用される。Brazeのログをユーザーに表示するには、これを有効にする。
- **OneTrustクッキーカテゴリー**：この設定により、[OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/)クッキーの同意グループをBrazeに関連付けることができる。

## サポートされている方法

Brazeは、RudderStackメソッドのidentify、track、screen、page、group、aliasをサポートしている。

{% tabs %}
{% tab 特定する %}

RudderStack[`identify` メソッドは](https://rudderstack.com/docs/destinations/marketing/braze/#identify)、ユーザーとそのアクションを関連付ける。RudderStackは、一意のユーザーIDと、名前、電子メール、IPアドレスなど、そのユーザーに関連するオプションの特徴をキャプチャする。

**特定コールのデルタ管理**<br>
デバイスモード経由でBrazeにイベントを送信する場合、`identify` コールを重複排除することでコストを節約できる。そのためには、ダッシュボードのDeduplicate Traits設定を有効にする。そしてRudderStackは、変更または修正された属性（trait）のみをBrazeに送信する。

**ユーザーを削除する**<br>
RudderStack[Data Regulation APIの](https://www.rudderstack.com/docs/api/data-regulation-api/) [Suppression with Deleteレギュレーションを](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation)使用して、Brazeでユーザーを削除できる。

{% endtab %}
{% tab トラック %}

RudderStackの[`track` メソッドは](https://rudderstack.com/docs/destinations/marketing/braze/#track)、すべてのユーザー・アクティビティと、それらのアクティビティに関連するプロパティをキャプチャする。

**注文完了**<br>
RudderStack Ecommerce API][20] を使用して、`Order Completed` という名前のイベントの track メソッドを呼び出すと、RudderStack はそのイベントにリストされている商品を [`purchases`][21].

{% endtab %}
{% tab スクリーン %}

RudderStackの[`screen` メソッドでは](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen)、ユーザーのモバイル画面表示を、表示画面に関する追加情報とともに記録することができる。

{% endtab %}
{% tab ページ %}

RudderStackの[`page` ](https://rudderstack.com/docs/destinations/marketing/braze/#page)、ウェブサイトのページビューを記録することができる。また、そのページに関するその他の関連情報もキャプチャする。

{% endtab %}
{% tab グループ %}

RudderStackの[`group` メソッドでは](https://rudderstack.com/docs/destinations/marketing/braze/#group)、ユーザーをグループに関連付けることができる。

**購読グループのステータス**<br>
サブスクリプショングループのステータスを更新するには、RudderStackダッシュボードの "Enable subscription groups in group call "設定を有効にし、グループコールでサブスクリプショングループのステータスを送信する。

{% endtab %}
{% tab 別名 %}

RudderStackの[`alias` メソッドでは](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias)、既知のユーザーの異なるIDをマージすることができる。RudderStackは、クラウドモードでのみBrazeのエイリアス呼び出しをサポートしていることに注意。

{% endtab %}
{% endtabs %}

## ユーザー特性をネストされたカスタム属性として送信する

ユーザー特性をネストされたカスタム属性としてBrazeに送信し、それに対して追加、更新、削除操作を実行できる。そのためには、RudderStackでBrazeデスティネーションを設定する際に、"Use Custom Attributes Operation dashboard "設定を有効にする。この機能はクラウドモードでのみ利用できる。

`identify` 、ネストされたカスタム・アトリビュートとして、以下のフォーマットでユーザーの特徴を送ることができる：
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

`track` 、`page` 、`screen` のコールでカスタムユーザー属性としてユーザー特性を送信するには、`traits` をイベントのコンテキストフィールドとして渡す：
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
更新と削除の操作では、`identifier` が必須キーとなる。add、update、remove操作が入れ子配列に存在しない場合、RudderStackはデフォルトでcreate操作を使用してプロパティを作成する。ネストされたカスタム属性の送信に関する詳細は、[オブジェクトの]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)配列を参照のこと。
{% endalert %}

[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}
[1]: https://rudderstack.com/
[3]: https://www.rudderstack.com/docs/dashboard-guides/sources/
[15]: {{site.baseurl}}/api/basics/#endpoints
[20]: https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/
[21]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]: https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started
\[android] ： https://github.com/rudderlabs/rudder-integration-braze-android
\[ios] ： https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master
\[swift] ： https://github.com/rudderlabs/rudder-integration-braze-swift
\[web] ： https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze
\[react] ： https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native
\[flutter] ： https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter