---
nav_title: WSC Sports
article_title: WSC Sports
description: "この参考記事では、BrazeとWSC Sportsの提携について説明しています。WSC Sportsはスポーツ動画プラットフォームであり、Brazeのプッシュ通知に豊かで強力なスポーツメディアを含めることができます。"
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> [WSC Sports][1]プラットフォームは、すべてのデジタルプラットフォームおよびすべてのスポーツファンのために、パーソナライズされたスポーツビデオを自動的かつリアルタイムで生成します。 

BrazeとWSC Sportsの統合により、Brazeプッシュ通知にリッチで堅牢なスポーツメディアを含めることができます。 

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| WSCアカウント | このパートナーシップを利用するには、WSCアカウントが必要です。 |
| Braze REST API キー | `users.track`の権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

WSC Sportsアプリケーションは、動画の選択からエンドユーザーのデバイスへのプッシュ通知の到着まで、エンドツーエンドのプロセスを処理します。 

### ステップ1:送信設定を選択

![][2]{: style="float:right;max-width:25%;margin-bottom:15px;"}

統合を開始する前に、Brazeで希望するキャンペーンとユーザーセグメントが構築されていることを確認してください。完了したら、WSC Sportsプラットフォームで希望する動画を選択し、送信設定で使用したいBrazeユーザーSegmentとキャンペーンIDを選択します。最後に、プッシュメッセージを送信したい時間を選択してください。 

#### APIコール

送信されると、WSC Sportsは選択されたオプションに基づいて、次のBrazeエンドポイントを使用して、選択されたユーザーセグメントにプッシュ通知を配信します:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- /メッセージ/送信

メッセージの本文は次のとおりです: 
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

この時点で、あなたのキャンペーンはテストと送信の準備ができているはずです。エラーに遭遇した場合は、Brazeエラーメッセージログを確認してください。 

[1]: https://wsc-sports.com/
[2]: {% image_buster /assets/img/wsc_sports/braze_integration.jpg %}「braze_integration.jpg」