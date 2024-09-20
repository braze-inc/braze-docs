---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "この参考文献は、Brazeと、世界中で最も人気のあるインスタントメッセージング プラットフォームの1つであるファック・eBook Messengerとの提携について概説している。"
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Fac eBook Messenger](https://developers.facebook.com/docs/messenger-platform/)は、世界中で最も人気のあるインスタントメッセージング プラットフォームの1つで、月間10億近くのアクティブユーザーで使用されています。このプラットフォームを通じて、ブランドは魅力的なチャットボットを作り出し、彼らの顧客と知的かつ自動的にやり取りすることができる。

Braze およびFac eBook インテグレーションは、Braze webhook、セグメンテーション、およびパーソナライゼーション、およびトリガー リング機能を活用して、Messenger プラットフォームAPI を介してFac eBook Messengerでユーザーに通知します。カスタムFac eBook Messenger Webhook テンプレートは、**テンプレート s**> **Webhook テンプレート s** のプラットフォームに含まれています。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Engagement**> **Templates &Media**> **Webフックテンプレート** に移動します。
{% endalert %}

Fac eBook Messenger プラットフォームは、"既存のトランスアクションを促進したり、他の顧客支援アクションを提供したり、人から要求された内容を配信したりする非プロモーションメッセージを意図しています。詳しくは、[Fac eBookのプラットフォームガイドライン](https://developers.facebook.com/docs/messenger-platform)および[許容ユースケースの例s](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable)を参照してください。

## 前提条件

統合を進める前に、以下を確認します。
- ファクスeBookでは、Messenger プラットフォームを使用してマーケティングを送信することはできません。 
- ユーザーの明示的な権限が必要になります。 
- FaceBook アプリのテストユーザーではないユーザーにメッセージを送信するには、アプリがFaceBookの[アプリレビュー](https://developers.facebook.com/docs/messenger-platform/app-review)に合格する必要があります。<br><br>

| 要件| Origin| アクセス| 説明|
| ---| ---| ---|
| ファクスeBook Messenger画面| Facebook| [https://<メタID="2" />/pages/create](https://www.facebook.com/pages/create) | Fac eBook ページがボットのID として使用されます。アプリとチャットすると、ページネームとプロファイルピクチャが表示されます。|
| ファックeBook Messenger アプリ| Facebook| [https://developers.facebook.com/アプリs](https://developers.facebook.com/apps) | Fac eBook アプリには、アクセストークンs を含むMessengerボットの設定s が含まれています。
| アプリボット審査・アプリ評価 | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | ボットを公開する準備ができたら、Fac eBook に送信して確認し、承認をアプリする必要があります。この審査の過程で、皆様のMessengerボットが、私たちの方針と機能を期待どおりに遵守し、Messengerの全員が利用できるようにすることができます。 |
| ページスコープID (PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | ファクスeBook Messengerで送信するには、ユーザーのPSIDが必要です。ユーザーがMessenger を介してアプリと通信すると、Fac eBook によってPSID が作成されます。このPSID は、ストリングカスタム属性としてBraze に送信できます。
| ページアクセストークン | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | これらのアクセストークンs は、ユーザー アクセストークンs に似ていますが、ファックページに属するデータの読み取り、書き込み、または変更を行う権限 API を提供する点が異なります。ページアクセストークンを取得するには、ユーザーアクセストークンを取得し、`manage_pagespermission`を要求する必要があります。ユーザーアクセストークンを取得したら、グラフAPI を使用してページアクセストークンを取得します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

BrazeファクトeBook Messenger Webhookの設定方法を以下に示します。
ボットのセットアップに追加のヘルプが必要な場合は、[ Braze GitHub リポジトリ](https://github.com/Appboy/appboy-fb-messenger-bot) に完全なMessengerボットチュートリアルとサンプルコードがあります。

### ステップ1:PSID を収集する

Fac eBook Messengerでメッセージを送信するには、ユーザーのページ固有ID (PSID) を収集して、ユーザーを識別し、一貫して対話する必要があります。PSID は、ユーザーのファクスeBookID とは異なります。Fac eBook は、顧客を表示したり、顧客を表示したりするたびに、この識別子を作成します。

PSID は、さまざまな[エントリポイント](https://developers.facebook.com/docs/messenger-platform/discovery) Fac eBook のいずれかを使用して見つけることができます。ユーザーがアプリにメッセージを送ったり、ボタンをアプリしたり、メッセージを送信したりといった対話のアクションを受け取った後は、そのPSIDが`sender.id`プロパティのWebhookの行動に含まれるため、ボットはアクションを受けた人を識別できます。

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

メッセージを送信するたびに、そのPSID がリクエストの`recipient.id` プロパティに含まれ、メッセージを受信するユーザを識別します。

### ステップ2:カスタム属性としてBrazeに送信

PSID を受信していると確信したら、これを開発者と調整して共有し、[カスタム属性]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes) としてPSID をBraze に送信します。PSID は、[API コール](https://developers.facebook.com/docs/messenger-platform/reference/send-api) でアクセスできる文字列です。

### ステップ3:Webhook テンプレートのセットアップ

**Templates & Media**から**Webフックテンプレート**に進み、**FaceBook Messenger Webフックテンプレート**を選択します。

1. テンプレートの名前を入力し、必要に応じてチームとタグs を追加します。
2. メッセージを入力するか、[Fac eBook](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages)で利用可能なメッセージテンプレートを選択します。また、[type](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types)または[タグ](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags)を選択することもできます。
3. カスタム属性としてPSID を含めます。これを行うには、**Request Body**ボックスの隅にある、青と白の**+**ボタンを使用します。
3. `FACEBOOK_PAGE_ACCESS_TOKEN` をトークンに置き換えて、Webhook URL にページアクセストークンを追加します。

#### Webhookのプレビューとテスト

Webhookを確認してから送信してください。Messenger ID がBraze に保存されていることを確認し(または、それを見つけてカスタマイズしたユーザーとしてテストする)、プレビューを使用してテストメッセージを送信します。

![Fac eBook Messenger Webhook テンプレートのTest タブでは、現存するユーザーに送信することでメッセージをプレビューできます。][60]

メッセージが正常に受信された場合は、配信設定s を設定できます。

## この統合の使用

設定が完了したら、このインテグレーションを使用してFac eBook Messenger ユーザー s を対象にします。ユーザー の電話番号を使用してメッセージを送信しておらず、繰り返しMessengerメッセージを送信する予定がない場合は、\[Messenger ID が存在するすべてのユーザーにSegment][62] を作成し、\[分析 "トラッキング][61]] をオンにして、Messenger サブスクリプションレートを経時的に追跡する必要があります。 

![セグメントフィルター"messenger_id"を"に設定すると空白"ではありません。][63]

Messenger サブスクライバーs に固有のSegmentを作成しない場合は、エラーs を回避するために、Messenger ID のフィルターを必ず含めてください。

他のセグメンテーションを使用して、他のキャンペーンと同様に、Messenger キャンペーンs、および残りのキャンペーン作成処理をターゲットにすることもできます。

[60]: {% image_buster /assets/img_archive/fbm-test.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}