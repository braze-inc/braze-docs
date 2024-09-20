---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "この参考記事では、Braze Currentsと企業向け顧客データプラットフォームであるTreasure Dataとのパートナーシップの概要を説明し、Brazeに直接ジョブ結果を書き込むことを可能にしている。"
page_type: partner
tool: Currents
search_tag: Partner


---


# Treasure Data for Currents


> [Treasure Dataは][1]顧客データプラットフォーム（CDP）であり、複数のソースから情報を収集し、マーケティングスタックの様々な場所にルーティングする。

BrazeとTreasure Dataの統合により、2つのシステム間の情報の流れをシームレスにコントロールすることができる。Currentsを使えば、データをTreasure Dataに接続し、成長スタック全体で実行可能なものにすることもできる。


## 前提条件


| 必要条件 | 説明 |
| ----------- | ----------- |
| Treasure Data | このパートナーシップを利用するには、[トレジャーデータのアカウントが][0]必要である。 |
| Currents | データをTreasure Dataにエクスポートするには、アカウントに[Braze Currentsを][2]設定する必要がある。 |
| トレジャーデータURL | これは、Treasure Dataのダッシュボードに移動し、取り込みURLをコピーすることで取得できる。|
{: .reset-td-br-1 .reset-td-br-2}


## 統合


Treasure Dataとの接続には、Postback APIを使用することを推奨する。この方法はデフォルトのコネクターを必要とせず、プッシュ方式でデータを受け取ることができる。1つのデータ・バッチで送信されるすべてのイベントは、JSON配列の1行の1フィールド内にあり、必要なデータを取得するために解析する必要がある。


{% alert important %}
現在のところ、イベントコレクターによるTreasure Dataへの取り込みはリアルタイムではなく、5分ほどかかることがある。
{% endalert %}


### ステップ1:BrazeでTreasure Data Postback APIをセットアップする


Postback APIの作成方法は、[Treasure Dataの][3]ウェブサイトに掲載されている。Brazeは、event-collectorを介した取り込みを除き、更新されたイベントをリアルタイムでTreasure Dataに直接送信する。完了すると、Treasure Dataは次のステップで使用するためにコピーするデータソースURLを提供する。


### ステップ2:電流を作る


Brazeで、**Current**>**\+ Create Current**>**Treasure Data Exportに**移動する。統合名、連絡先Eメール、Treasure Data URLを入力する。次に、利用可能なイベントのリストから追跡したいものを選択し、**「Launch Current**」をクリックする。


Treasure Data に送信されるすべてのイベントには、ユーザーの`external_user_id` が含まれる。現時点では、Brazeは、`external_user_id` を設定していないユーザーのイベントデータをTreasure Dataに送信しない。


{% alert important %}
トレジャーデータのURLを常に最新の状態に保つ。コネクタのURLが正しくない場合、Brazeはイベントを送信できない。この状態が48時間以上続くと、コネクタのイベントは削除され、データは永久に失われる。
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


Brazeは、[Currentsイベント用語集に]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents)記載されているすべてのデータ（[メッセージエンゲージメントイベントと]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) [顧客行動]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)イベントの両方のすべてのプロパティを含む）のTreasure Dataへのエクスポートをサポートしている。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクターのペイロード構造と同じで、[カスタムHTTPコネクターのサンプルリポジトリで](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)見ることができる。


[0]: https://console.treasuredata.com/users/sign_in
[1]: https://www.treasuredata.com/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents
[3]: https://docs.treasuredata.com/display/public/PD/Postback+API
[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}