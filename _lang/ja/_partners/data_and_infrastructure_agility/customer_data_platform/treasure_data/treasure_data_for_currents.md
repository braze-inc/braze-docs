---
nav_title: Treasure Data for Currents
article_title:Treasure Data for Currents
description:この記事では、Braze CurrentsとTreasure Dataのパートナーシップについて説明します。Treasure Dataは、ジョブの結果を直接Brazeに書き込むことができるエンタープライズ顧客データプラットフォームです。
page_type: partner
tool:Currents
search_tag:Partner


---


# Treasure Data for Currents


> [トレジャーデータ][1]は、複数のソースから情報を収集し、マーケティングスタック内のさまざまな他の場所にルーティングするカスタマーデータプラットフォーム（CDP）です。

BrazeとTreasure Dataの統合により、両システム間の情報の流れをシームレスに制御できます。Currentsを使用すると、データをTreasure Dataに接続して、成長スタック全体で実行可能にすることもできます。


## 前提条件


| 要件 | 説明 |
| ----------- | ----------- |
| Treasure Data | [Treasure Data アカウント][0]がこのパートナーシップを利用するために必要です。 |
| Currents | データをTreasure Dataにエクスポートするには、アカウントに[Braze Currents][2]を設定する必要があります。 |
| トレジャーデータURL | これは、Treasure Data ダッシュボードに移動し、インジェスト URL をコピーすることで取得できます。|
{: .reset-td-br-1 .reset-td-br-2}


## 統合


推奨されるTreasure Dataとの接続方法は、Postback APIを通じて行うことです。この方法ではデフォルトのコネクタを必要とせず、プッシュアプローチでデータを受信できます。すべてのイベントは、1つのデータバッチで送信され、JSON配列の1つの行の1つのフィールド内にあり、必要なデータを取得するために解析する必要があります。


{% alert important %}
イベントコレクターを通じたTreasure Dataへの取り込みは現在リアルタイムでは行われておらず、最大で5分かかる場合があります。
{% endalert %}


### ステップ1:ブラゼでトレジャーデータのポストバックAPIを設定する


Postback APIの作成手順は、[Treasure Data][3]のウェブサイトで確認できます。Brazeは、イベントコレクターを介した取り込みを除いて、更新されたイベントをリアルタイムでTreasure Dataに直接送信します。完了すると、Treasure Dataは次のステップで使用するためにコピーするデータソースURLを提供します。


### ステップ2:作成 現在


Brazeで、**Currents** > **\+ Create Current** > **Treasure Data Export**に移動します。統合名、連絡先メール、およびTreasure Data URLを提供してください。次に、利用可能なイベントのリストから追跡したいものを選択し、**現在の起動**をクリックします。


Treasure Dataに送信されるすべてのイベントには、ユーザーの`external_user_id`が含まれます。現時点では、Brazeは`external_user_id`を設定していないユーザーのイベントデータをTreasure Dataに送信しません。


{% alert important %}
最新のTreasure Data URLを維持してください。コネクタのURLが間違っている場合、Brazeはイベントを送信できません。これが48時間以上続く場合、コネクタのイベントはドロップされ、データは永久に失われます。
{% endalert %}


#### 例のイベントフィールド値
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


Brazeは、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents)（[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)および[顧客行動]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)イベントのすべてのプロパティを含む）に記載されているすべてのデータをTreasure Dataにエクスポートすることをサポートしています。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクタのペイロード構造と同じであり、[カスタムHTTPコネクタの例のリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。


[0]: https://console.treasuredata.com/users/sign_in
[1]: https://www.treasuredata.com/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents
[3]: https://docs.treasuredata.com/display/public/PD/Postback+API
[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}