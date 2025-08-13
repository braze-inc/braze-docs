---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "このリファレンス記事では、Braze と Facebook Messenger のパートナーシップについて説明します。Facebook Messenger は、世界で最も人気があるインスタントメッセージプラットフォームの1つです。"
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) は、世界で最も人気があるインスタントメッセージングプラットフォームの1つで、1か月あたりのアクティブユーザー数は10億にのぼります。ブランドはこのプラットフォームで、顧客とインテリジェントかつ自動的にやり取りするための魅力的なチャットボットを作成します。

Braze とFacebook の統合では、Messenger Platform API を介して Facebook Messenger のユーザーにメッセージを送信するために、Braze Webhook、セグメンテーション、パーソナライゼーション、トリガー機能が利用されます。カスタム Facebook Messenger Webhook テンプレートは、Braze プラットフォームの [**テンプレート**] > [**Webhook テンプレート**] にあります。

Facebook Messenger プラットフォームは、「既存の取引を促進し、他の顧客サポートアクションを提供し、個人が要求したコンテンツを配信する非プロモーションメッセージ」を対象としています。詳細については、[Facebook のプラットフォームガイドライン](https://developers.facebook.com/docs/messenger-platform)と[許容可能なユースケースの例](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable)を参照してください。

## 前提条件

統合を進める前に、以下を確認します。
- Facebook では、マーケティングメッセージの送信に Messenger プラットフォームを使用することを許可していません。 
- お客様のページからのメッセージに対するユーザーの明示的な許可が必要になります。 
- FaceBook アプリのテストユーザーではないユーザーにメッセージを送信するには、アプリがFaceBookの[アプリレビュー](https://developers.facebook.com/docs/messenger-platform/app-review)に合格する必要があります。<br><br>

| 必要条件| 提供元| アクセス| 説明|
| ---| ---| ---|
| Facebook Messenger ページ| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Facebook ページがボットの ID として使用されます。アプリとチャットすると、ページ名とプロファイル画像が表示されます。|
| Facebook Messenger アプリ| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Facebook アプリには、アクセストークンなどの Messenger ボットの設定が含まれています。
| アプリボットの審査と承認 | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | ボットを公開する準備ができたら、審査と承認を受けるために Facebook に提出する必要があります。す。この審査の過程で、皆様のMessengerボットが、私たちの方針と機能を期待どおりに遵守し、Messengerの全員が利用できるようにすることができます。 |
| ページスコープ ID (PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Facebook Messenger でメッセージを送信するには、ユーザー PSID が必要です。ユーザーが Messenger を介してアプリとやり取りするときに、Facebook によって PSID が作成されます。このPSID は、ストリングカスタム属性としてBraze に送信できます。
| ページアクセストークン | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | これらのアクセストークンは、Facebook Page に属するデータの読み取り、書き込み、変更を行う API に権限を付与することを除き、ユーザーアクセストークンと似ています。ページアクセストークンを取得するには、ユーザーアクセストークンを取得し、`manage_pagespermission` を要求する必要があります。ユーザーアクセストークンを取得したら、Graph API を使用してページアクセストークンを取得できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

以下に、Braze Facebook Messenger Webhook の設定方法を示します。
ボットのセットアップに追加のヘルプが必要な場合は、[ Braze GitHub リポジトリ](https://github.com/Appboy/appboy-fb-messenger-bot) に完全なMessengerボットチュートリアルとサンプルコードがあります。

### ステップ1:PSID を収集する

Facebook Messenger でメッセージを送信するには、ユーザーを識別し、一貫したやり取りを行うためにユーザーのページ固有の ID (PSID) を収集する必要があります。PSID はユーザーの Facebook ID とは異なります。顧客にメッセージを送信する場合または顧客からメッセージが送信される場合は常に、Facebook によりこの ID が作成されます。

PSID は、Facebook が提供するさまざまな[エントリポイント](https://developers.facebook.com/docs/messenger-platform/discovery)の1つを使用して確認できます。ユーザーがアプリにメッセージを送ったり、ボタンをアプリしたり、メッセージを送信したりといった対話のアクションを受け取った後は、そのPSIDが`sender.id`プロパティのWebhookの行動に含まれるため、ボットはアクションを受けた人を識別できます。

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

PSID を受信していると確信したら、これを開発者と調整して共有し、[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#custom-attributes) としてPSID をBraze に送信します。PSID は、[API コール](https://developers.facebook.com/docs/messenger-platform/reference/send-api) でアクセスできる文字列です。

### ステップ 3:Webhook テンプレートのセットアップ

**Templates & Media**から**Webフックテンプレート**に進み、**FaceBook Messenger Webフックテンプレート**を選択します。

1. テンプレートの名前を入力し、必要に応じてチームとタグs を追加します。
2. メッセージを入力するか、[Facebook で利用可能なメッセージテンプレート](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages)からメッセージテンプレートを選択します。また、[タイプ](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types)や[タグ](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags)を選択することもできます。
3. カスタム属性としてPSID を含めます。これを行うには、**Request Body**ボックスの隅にある、青と白の**+**ボタンを使用します。
3. `FACEBOOK_PAGE_ACCESS_TOKEN` をトークンに置き換えて、Webhook URL にページアクセストークンを追加します。

#### Webhookのプレビューとテスト

Webhookを確認してから送信してください。Messenger ID がBraze に保存されていることを確認し(または、それを見つけてカスタマイズしたユーザーとしてテストする)、プレビューを使用してテストメッセージを送信します。

![Facebook Messenger Webhook テンプレートの「Test」タブ。既存のユーザーにメッセージを送信することでそのメッセージをプレビューできる。]({% image_buster /assets/img_archive/fbm-test.png %})

メッセージが正常に受信された場合は、配信設定s を設定できます。

## この統合を使う

設定が完了したら、この統合を使用して Facebook Messenger ユーザーをターゲットにします。ユーザーの電話番号を使用してメッセージを送信しておらず、Messenger メッセージを繰り返し送信する予定がある場合は、Messenger ID がカスタム属性として存在するすべてのユーザーに対して[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment)し、[分析の追跡]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/)をオンにして、Messenger のサブスクリプション率を経時的に追跡する必要があります。 

![セグメントフィルター「messenger_id」が「is not blank」に設定されている。]({% image_buster /assets/img_archive/fbm-segmentation.png %})

Messenger サブスクライバー向けの特定のセグメントを作成しない場合は、エラーを避けるために、既存の Messenger ID のフィルターを必ず含めてください。

他のセグメンテーションを使用して Messenger キャンペーンをターゲットにし、他のキャンペーンと同様にそれ以降のキャンペーン作成プロセスを実行することもできます。

