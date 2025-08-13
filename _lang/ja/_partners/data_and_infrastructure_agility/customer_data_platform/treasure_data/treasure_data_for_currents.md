---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "この参考記事では、Braze Currentsと企業向け顧客データプラットフォームであるTreasure Dataとのパートナーシップの概要を説明し、Brazeに直接ジョブ結果を書き込むことを可能にしている。"
page_type: partner
tool: Currents
search_tag: Partner


---


# Treasure Data for Currents

> [トレジャーデータ][1]は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまな場所に情報をルーティングする顧客データプラットフォーム (CDP) です。

Braze とトレジャーデータの統合により、2 つのシステム間の情報の流れをシームレスに制御できます。Currents では、データをトレジャーデータに接続し、グローススタック全体で実用的なデータにすることもできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| トレジャーデータ | このパートナーシップを活用するには、[トレジャーデータのアカウント][0]が必要です。 |
| Currents | トレジャーデータにデータを再度エクスポートするには、アカウントに [Braze Currents][2] を設定する必要があります。 |
| トレジャーデータ URL | これは、トレジャーデータのダッシュボードに移動し、取り込み URL をコピーすることで取得できます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
トレジャーデータは各イベントを一括してログに記録します。トレジャーデータを照会してイベントカウントを取得する方法の詳細については、「[Braze Currents のインポート統合](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration)」を参照してください。
{% endalert %}

## 統合

トレジャーデータとの接続には、Postback API を使用することをお勧めします。この方法はデフォルトのコネクターを必要とせず、プッシュ方式でデータを受け取ることができる。1つのデータバッチで送信されるすべてのイベントは、JSON 配列の1つの行の1つのフィールド内にあり、必要なデータを取得するために解析する必要があります。

{% alert important %}
現時点では、イベントコレクターを介したトレジャーデータへの取り込みはリアルタイムでは行われず、最大5分かかることがあります。
{% endalert %}

### ステップ1:Braze を使用してトレジャーデータの Postback API を設定する

Postback API の作成方法については、[トレジャーデータ][3]の Web サイトを参照してください。Braze は、イベントコレクターによる取り込みを除き、更新されたイベントをリアルタイムでトレジャーデータに直接送信します。完了すると、トレジャーデータからデータソース URL が提供されます。この URL をコピーして、次のステップで使用します。

### ステップ2:Current を作成する

Braze で [**Currents**] > [**\+ Current を作成**] > [**トレジャーデータのエクスポート**] に移動します。統合名、連絡先メール、およびトレジャーデータ URL を指定します。次に、利用可能なイベントのリストから追跡したいものを選択し、**「Launch Current**」をクリックする。

トレジャーデータに送信されるすべてのイベントには、ユーザーの `external_user_id` が含まれます。この時点では Braze は、`external_user_id` が設定されていないユーザーのイベントデータをトレジャーデータに送信しません。

{% alert important %}
トレジャーデータ URL を最新の状態に保ちます。コネクタのURLが正しくない場合、Brazeはイベントを送信できない。この状態が48時間以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

#### イベント・フィールドの値の例
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### インジェストされたビューの例

![4]{: style="max-width:70%;"}

## 統合の詳細

Braze では、「[Currents イベント用語集]({{site.baseurl}}/user_guide/data/braze_currents/)」にリストされているすべてのデータ ([メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)イベントおよび[顧客行動]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)イベントのすべてのプロパティを含む) をトレジャーデータにエクスポートできます。

エクスポートされたデータのペイロードの構造は、カスタム HTTP コネクターのペイロード構造と同じです。これは、[カスタム HTTP コネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。


[0]: https://console.treasuredata.com/users/sign_in
[1]: https://www.treasuredata.com/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents
[3]: https://docs.treasuredata.com/display/public/PD/Postback+API
[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
