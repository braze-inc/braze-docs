---
nav_title: RudderStack
article_title: RudderStack
description: "この記事では、Brazeと、Android、iOS、WebアプリケーションにBrazeのシームレスな統合を提供するオープンソースの顧客データ基盤であるRudderStackとのパートナーシップについて概説する。RudderStackを使えば、アプリ内の顧客イベントデータをBrazeに直接送信し、コンテキスト分析を行うことができる。"
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) は、顧客イベントデータを収集し、希望するデータウェアハウスや Braze などの他の多数の分析プロバイダーにルーティングするための、オープンソースの顧客データインフラです。これはエンタープライズ対応で、イベントデータを即座に処理するための強力な変換フレームワークを提供します。

Braze と RudderStack の統合により、Android、iOS、および Web アプリケーションのネイティブ SDK 統合と、バックエンドサービスからのサーバー間統合が提供されます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| RudderStackアカウント | このパートナーシップを活用するには、[RudderStack アカウント](https://app.rudderstack.com/)が必要です。 |
| 設定済みのソース | [ソース](https://www.rudderstack.com/docs/dashboard-guides/sources/)は基本的に、Web サイト、モバイルアプリ、バックエンドサーバーなど、RudderStack に送信されるあらゆるデータの提供元です。RudderStack で Braze を宛先として設定する前に、ソースを設定する必要があります。 |
| Braze REST API キー | `users.track`、`users.identify`、`users.delete`、`users.alias.new` の権限を持つ Braze REST API キー。<br><br>これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Brazeアプリのキー | Brazeダッシュボードでアプリキーを取得するには、**「設定」**>「**アプリ設定**」>「**識別**」と進み、アプリ名を見つける。関連する識別子文字列を保存する。
| データセンター | データセンターは、Braze ダッシュボード [インスタンス]({{site.baseurl}}/api/basics/#endpoints)に対応しています。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

### ステップ1:ソースを追加する

Brazeへのデータ送信を開始するには、まずRudderStackアプリにソースが設定されていることを確認する必要がある。データソースの設定方法については、[RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) を参照のこと。

### ステップ2: 宛先を設定する

データソースが設定されたので、RudderStack ダッシュボードで、[**Destinations**] の下にある [**ADD DESTINATION**] を選択します。使用可能な宛先のリストから [**Braze**] を選択し、[**Next**] をクリックします。

Brazeデスティネーションで、アプリキー、Braze REST APIキー、データクラスタ、およびネイティブSDKオプション（デバイスモードのみ）を指定する。ネイティブ SDK オプションをオンにすると、Braze ネイティブ SDK を使用してイベントが送信されます。 

![]({% image_buster /assets/img/RudderStack/braze_settings.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

### ステップ 3: 統合のタイプを選ぶ

次のいずれかの方法を使用して、RudderStack の Web ライブラリとネイティブクライアント側ライブラリを Braze と統合できます。

- [サイドバイサイド/デバイスモード](#device-mode)**:**RudderStackは、クライアント（ブラウザまたはモバイルアプリケーション）から直接Brazeにイベントデータを送信する。
- [サーバー間/クラウドモード](#cloud-mode)**:**Braze SDK はイベントデータを RudderStack に直接送信します。イベントデータは変換され、Braze にルーティングされます。
- [ハイブリッドモード](#hybrid-mode)**:**ハイブリッドモードを使用して、iOSとAndroidの自動生成イベントとユーザー生成イベントを、単一の接続を使用してBrazeに送信する。

{% alert note %}
RudderStack の[接続モード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/)と、それぞれの利点について詳しく説明します。
{% endalert %}

#### サイドバイサイド統合 (デバイスモード) {#device-mode}

このモードでは、Web サイトまたはモバイルアプリで設定した Braze SDK を使用して、イベントを Braze に送信できます。

「[サポートされているメソッド](#supported-methods)」で説明するように、Braze の GitHub リポジトリでご使用のプラットフォームに対応した RudderStack SDK へのマッピングを設定します。

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

デバイスモードの統合を完了するには、Rudderstack の[プロジェクトに Brazeを追加する](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration)詳しい手順を参照してください。

#### サーバー間統合（クラウドモード） {#cloud-mode}

このモードでは、SDKはイベントデータを直接RudderStackサーバーに送信する。そして、RudderStackはこのデータを変換し、目的の目的地にルーティングする。この変換は、RudderStack のトランスフォーマーモジュールを使用して RudderStack バックエンドで実行されます。

統合を有効にするには、[サポートされているメソッド](#supported-methods)で説明されているように、RudderStack メソッドを Braze にマッピングする必要があります。

{% alert note %}
RudderStackのサーバーサイドSDK（Java、Python、Node.js 、Go、Ruby）は、クラウドモードのみをサポートしている。これは、サーバー側の SDK が RudderStack バックエンドで動作し、Braze 固有のSDK を読み込むことができないためです。
{% endalert %}

{% alert important %}
サーバー間の統合は、プッシュ通知やアプリ内メッセージングなどのBraze UI機能をサポートしていない。ただし、これらの機能はデバイスモード統合によってサポートされます。
{% endalert %}

#### ハイブリッドモード {#hybrid-mode}

ハイブリッドモードを使用して、iOSとAndroidのソースからすべてのイベントをBrazeに送信する。 

ハイブリッドモードで Braze にイベントを送信することを選択した場合、RudderStack により次の操作が行われます。
1. Braze SDKを初期化する。
2. ユーザーが生成したすべてのイベント（identify、track、page、screen、group）をクラウドモードからのみBrazeに送信し、デバイスモードからの送信をブロックする。
3. 自動生成イベント（アプリ内メッセージ、Braze SDKを必要とするプッシュ通知）をデバイスモード経由で送信する。

[ハイブリッドモードでイベントを送信する](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode)には、ソースを Braze の宛先に接続している状態でハイブリッドモードオプションを使用します。次に、Brazeインテグレーションをプロジェクトに追加する。

## ステップ4:追加設定を行う

初期設定完了後、Brazeでデータを正しく受信するために以下の設定を行う：

- **グループ通話でサブスクリプショングループを有効にする**：グループイベントでサブスクリプショングループのステータスを送信するには、この設定を有効にします。詳細については、[Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group) を参照してください。
- **Use Custom Attributes Operation**:Brazeの[ネストされたカスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)機能を使用してセグメントを作成し、カスタム属性オブジェクトを使用してメッセージをパーソナライズする場合は、この設定を有効にする。詳細については、[ネストされたカスタム属性としてユーザー特性を送信するを](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes)参照のこと。
- **Track events for anonymous users**:この設定を有効にすると、匿名のユーザーの活動が追跡され、その情報がBrazeに送信される。

### デバイスモード設定

以下の設定は、[デバイスモード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode)経由でBrazeにイベントを送信する場合にのみ適用される：

- **クライアント側のイベントフィルタリング**：この設定により、Brazeに流れるイベントをブロックするか、許可するかを指定できる。この設定の詳細については、[クライアント側のイベントフィルタリング](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/)を参照してください。
- **Deduplicate Traits**:この設定を有効にすると、[`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify) 呼び出しでユーザー特性の重複が排除されます。
- **Show Braze logs**:この設定は、[JavaScript SDKを](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/)ソースとして使用する場合にのみ適用される。Brazeのログをユーザーに表示するには、これを有効にする。
- **OneTrustクッキーカテゴリー**：この設定により、[OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/)クッキーの同意グループをBrazeに関連付けることができる。

## サポートされている方法

Brazeは、RudderStackメソッドのidentify、track、screen、page、group、aliasをサポートしている。

{% tabs %}
{% tab Identify %}

RudderStack[`identify` メソッドは](https://rudderstack.com/docs/destinations/marketing/braze/#identify)、ユーザーとそのアクションを関連付ける。RudderStackは、一意のユーザーIDと、名前、電子メール、IPアドレスなど、そのユーザーに関連するオプションの特徴をキャプチャする。

**identify 呼び出しの差分管理**<br>
デバイスモードで Braze にイベントを送信する場合、`identify` 呼び出しを重複排除することでコストを節減できます。そのためには、[Deduplicate Traits] ダッシュボード設定を有効にします。その後、RudderStack は変更された属性 (特性) のみを Braze に送信します。

**ユーザーの削除**<br>
RudderStack [Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/) の[抑制と削除の規則 (Suppression with Delete regulation)](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) を使用して、Braze のユーザーを削除できます。

{% endtab %}
{% tab Track %}

RudderStackの[`track` メソッドは](https://rudderstack.com/docs/destinations/marketing/braze/#track)、すべてのユーザー・アクティビティと、それらのアクティビティに関連するプロパティをキャプチャする。

**Order completed**<br>
[RudderStack Ecommerce API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) を使用して `Order Completed` という名前のイベントに対して track メソッドを呼び出すと、RudderStack はそのイベントにリストされている製品を [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data). として Braze に送信します。

{% endtab %}
{% tab スクリーン %}

RudderStack の [`screen` メソッド](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen)を使用して、ユーザーのモバイル画面ビューを、表示されている画面に関する追加情報とともに記録できます。

{% endtab %}
{% tab ページ %}

RudderStack の [`page` メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#page) を使用して、Web サイトのページビューを記録できます。また、そのページに関するその他の関連情報もキャプチャされます。

{% endtab %}
{% tab Group %}

RudderStackの[`group` メソッドでは](https://rudderstack.com/docs/destinations/marketing/braze/#group)、ユーザーをグループに関連付けることができる。

**サブスクリプショングループのステータス**<br>
サブスクリプショングループのステータスを更新するには、RudderStack ダッシュボードの [Enable subscription groups in group call] 設定を有効にし、グループ呼び出しでサブスクリプショングループのステータスを送信します。

{% endtab %}
{% tab 別名 %}

RudderStack の [`alias` メソッド](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) を使用して、既知のユーザーの複数の ID をマージできます。RudderStack は、クラウドモードでのみ Braze のエイリアス呼び出しをサポートしていることに注意してください。

{% endtab %}
{% endtabs %}

## ユーザー特性をネストされたカスタム属性として送信する

ユーザー特性をネストされたカスタム属性としてBrazeに送信し、それに対して追加、更新、削除操作を実行できる。これを行うには、Braze の宛先を設定するときに Rudderstack で [Use Custom Attributes Operation dashboard] 設定を有効にします。この機能はクラウドモードでのみ利用できる。

次の形式で `identify` イベントでユーザー特性を階層化カスタム属性として送信できます。
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

`track`、`page`、または`screen` 呼び出しでユーザー特性をカスタムユーザ属性として送信するには、イベントのコンテキストフィールドとして `traits` を渡します。
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
更新と削除の操作では、`identifier` が必須キーとなる。add、update、remove操作が入れ子配列に存在しない場合、RudderStackはデフォルトでcreate操作を使用してプロパティを作成する。階層化カスタム属性の送信の詳細については、「[オブジェクト配列]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)」を参照してください。
{% endalert %}

