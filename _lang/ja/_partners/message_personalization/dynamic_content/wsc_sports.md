---
nav_title: WSC Sports
article_title:WSCスポーツ
description:「この参考記事では、BrazeとWSC Sportsとのパートナーシップについて概説しています。WSC Sportsは、Brazeのプッシュ通知に豊富で強力なスポーツメディアを含めることができるスポーツ動画プラットフォームです。「
alias: /partners/wsc_sports/
page_type: partner
search_tag:Partner

---

# WSCスポーツ

> [WSC Sportsプラットフォームは][1]、すべてのデジタルプラットフォームとすべてのスポーツファン向けにパーソナライズされたスポーツビデオを自動的かつリアルタイムで生成します。 

Braze と WSC Sports の統合により、Braze プッシュ通知にリッチでパワフルなスポーツメディアを含めることができます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| WSC アカウント | このパートナーシップを利用するには、WSC アカウントが必要です。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

WSC Sports アプリケーションは、動画の選択からエンドユーザーのデバイスへのプッシュ通知の到着まで、エンドツーエンドのプロセスを処理します。 

### ステップ1:送信設定を選択する

![][2]{: style="float:right;max-width:25%;margin-bottom:15px;"}

統合を開始する前に、目的のキャンペーンとユーザーセグメントが Braze に組み込まれていることを確認してください。完了したら、WSC Sportsプラットフォーム目的の動画を選択し、送信設定で使用したいBrazeユーザーSegment とキャンペーン IDを選択します。最後に、プッシュメッセージを送信する時間を選択します。 

#### API コール

送信されると、WSC Sportsは、選択したオプションに基づいて、次のBrazeエンドポイントを使用して、選択したユーザーセグメントにプッシュ通知を配信します。
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

結果のメッセージ本文は次のとおりです。 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### ステップ2:テスト送信

これで、キャンペーンをテストして送信する準備が整いました。エラーが発生した場合は、Braze エラーメッセージログを確認してください。 

[1]: https://wsc-sports.com/
[2]: {% image_buster /assets/img/wsc_sports/braze_integration.jpg %} 「braze_integration.jpg」