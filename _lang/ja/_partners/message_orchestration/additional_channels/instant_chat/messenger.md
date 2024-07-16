---
nav_title: Messenger
article_title:Facebook Messenger
alias: /partners/messenger/
description:この記事では、世界で最も人気のあるインスタントメッセージングプラットフォームの1つであるFacebook MessengerとBrazeのパートナーシップについて説明します。
page_type: partner
search_tag:Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) は、世界で最も人気のあるインスタントメッセージングプラットフォームの1つで、毎月約10億人のアクティブユーザーが利用しています。このプラットフォームを通じて、ブランドは顧客とインテリジェントかつ自動的に対話する魅力的なチャットボットを作成できます。

BrazeとFacebookの統合は、BrazeのWebhook、セグメンテーション、パーソナライゼーション、およびトリガー機能を活用して、Messenger Platform APIを通じてFacebook Messengerでユーザーにメッセージを送信します。カスタムFacebook Messenger Webhookテンプレートは、**テンプレート** > **Webhookテンプレート**の下にあるプラットフォームに含まれています。

{% alert note %}
古いナビゲーションを使用している場合は、[エンゲージメント]({{site.baseurl}}/navigation) > **テンプレートとメディア** > **Webhookテンプレート**に移動します。
{% endalert %}

Facebook Messengerプラットフォームは、「既存の取引を促進する非プロモーションメッセージ、他のカスタマーサポートアクションを提供するメッセージ、または人が要求したコンテンツを配信するメッセージ」を目的としています。続きを読むには、[Facebookのプラットフォームガイドライン](https://developers.facebook.com/docs/messenger-platform)と[許容される使用例の例](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable)をご覧ください。

## 前提条件

統合を進める前に次の点を確認してください:
- Facebookは、Messengerプラットフォームを使用してマーケティングメッセージを送信することを許可していません。 
- ページからのメッセージにはユーザーの明示的な許可が必要です。 
- Facebookアプリのテストユーザーではないユーザーにメッセージを送信するには、アプリがFacebookの[アプリレビュー](https://developers.facebook.com/docs/messenger-platform/app-review)に合格する必要があります。<br><br>

| 要件| 起源| アクセス| 説明|
| ---| ---| ---|
| Facebook Messengerページ| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Facebookページがあなたのボットのアイデンティティとして使用されます。人々があなたのアプリとチャットするとき、ページ名とプロフィール写真が表示されます。|
| Facebook Messenger アプリ| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Facebookアプリには、アクセス トークンを含むMessengerボットの設定が含まれています。
| アプリボットのレビューと承認 | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | あなたのボットを一般公開する準備ができたら、レビューと承認のためにFacebookに提出する必要があります。このレビュー プロセスにより、Messenger ボットがポリシーに準拠し、Messenger で誰でも利用できるようにする前に期待どおりに機能することを確認できます。 |
| ページスコープID（PSID） | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Facebook Messengerでメッセージを送信するには、ユーザーのPSIDが必要です。ユーザーがMessengerを介してアプリとやり取りすると、FacebookはPSIDを作成します。このPSIDは、文字列のカスタム属性としてBrazeに送信できます。
| ページアクセス トークン | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | これらのアクセス トークンはユーザー アクセス トークンと似ていますが、Facebook ページに属するデータを読み取り、書き込み、または変更する API への権限を提供する点が異なります。ページアクセス トークンを取得するには、ユーザー アクセス トークンを取得し、`manage_pagespermission`を要求する必要があります。ユーザーアクセス トークンを取得した後、Graph API を介してページアクセス トークンを取得します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

次の手順は、Braze Facebook MessengerのWebhookを設定する方法を示しています。
ボットのセットアップに追加のヘルプが必要な方のために、完全なMessengerボットのチュートリアルとサンプルコードが[Braze GitHubリポジトリ](https://github.com/Appboy/appboy-fb-messenger-bot)にあります！

### ステップ1:PSIDを収集する

Facebook Messengerでメッセージを送信するには、ユーザー' page-specific IDs (PSIDs) to identify your user and interact with them consistently. PSIDs are not the same as the user'のFacebook IDを収集する必要があります。Facebookは、顧客にメッセージを送信するたび、または顧客があなたにメッセージを送信するたびにこの識別子を作成します。

PSIDは、Facebookが提供するさまざまな[エントリーポイント](https://developers.facebook.com/docs/messenger-platform/discovery)の1つを使用して見つけることができます。ユーザーがアプリにメッセージを送信したり、ボタンをタップしたりメッセージを送信したりするなどのアクションを会話で行った後、そのPSIDはWebhookイベントの`sender.id`プロパティに含まれるため、ボットは誰がアクションを実行したかを識別できます。

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

メッセージを送信するたびに、誰がメッセージを受信するかを識別するために、リクエストの`recipient.id`プロパティに彼らのPSIDが含まれます。

### ステップ2:Brazeにカスタム属性として送信

PSIDを受信していることを確認したら、開発者と調整してPSIDをBrazeに[カスタム属性]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes)として送信してください。PSIDは[APIコール](https://developers.facebook.com/docs/messenger-platform/reference/send-api)を行うことでアクセスできる文字列です。

### ステップ3:Webhookテンプレートを設定する

**テンプレートとメディア**から**Webhookテンプレート**に移動し、**Facebook Messenger Webhookテンプレート**を選択します。

1. テンプレート名を提供し、必要に応じてチームとタグを追加します。
2. メッセージを入力するか、[Facebookで利用可能なテンプレートからメッセージを選択してください](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages)。メッセージの[タイプ](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types)や[タグ](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags)を選択することもできます。
3. PSIDをカスタム属性として含めます。これは、**+** コーナーの青と白のボタンを使用して、**リクエストボディ** ボックスで行うことができます。
3. Webhook URL にページ アクセス トークンを追加し、`FACEBOOK_PAGE_ACCESS_TOKEN` をトークンに置き換えます。

#### Webhook のプレビューとテスト

メッセージを送信する前に、Webhookをテストしてください。Messenger IDがBrazeに保存されていることを確認する（またはそれを見つけてカスタマイズされたユーザーとしてテストする）、そしてプレビューを使用してテストメッセージを送信する：

![Facebook MessengerのWebhookテンプレートのテストタブでは、既存のユーザーにメッセージを送信してプレビューできることを示しています。][60]

メッセージを正常に受信した場合は、その配信設定を構成できます。

## この統合を使用する

セットアップが完了したら、この統合を使用してFacebook Messengerユーザーをターゲットにします。ユーザーの電話番号を使用してメッセージを送信しておらず、Messengerメッセージを繰り返し送信する予定がある場合は、Messenger IDがカスタム属性として存在するすべてのユーザーのために\[セグメント][62]を作成し、\[分析トラッキング][61]をオンにして、時間の経過とともにMessengerの購読率を追跡する必要があります。 

![セグメントフィルター「messenger_id」が「空ではない」に設定されています。][63]

メッセンジャーの購読者のために特定のセグメントを作成しないことを選択した場合、エラーを避けるためにメッセンジャーIDが存在するフィルターを含めるようにしてください。

メッセンジャーキャンペーンをターゲットにするために他のセグメンテーションを使用することもできます。また、他のキャンペーンと同様に、キャンペーン作成プロセスの残りの部分も同様です。

[60]: {% image_buster /assets/img_archive/fbm-test.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}