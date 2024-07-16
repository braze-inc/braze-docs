---
nav_title: LINE
article_title:ライン
alias: /partners/line/
description:「この参考記事では、Brazeと世界で最も人気のあるインスタントメッセージングプラットフォームの1つであるLINEとのパートナーシップについて概説しています。「
page_type: partner
search_tag:Partner

---

# ライン

> [LINEは](https://line.me/en/)、世界で最も人気のあるインスタントメッセージングプラットフォームの1つで、月間数億人のアクティブユーザーが使用しています。このプラットフォームを通じて、ブランドは豊富な双方向のメッセージングで顧客と交流することができます。

[BrazeとLINEの統合により、BrazeのWebhook、高度なセグメンテーション、パーソナライゼーション、トリガー機能を活用して、LINE Messメッセージング APIを通じてLINEのユーザーにメッセージを送ることができます。](https://developers.line.biz/en/docs/messaging-api/overview/)

## 前提条件

LINEでは、ブランドがユーザーの同意を得ている限り、プロモーションメッセージと非プロモーションメッセージの両方をユーザーに送信できます。ユーザーにメッセージを送信するには、次の 2 つの条件のいずれかを満たす必要があります。
- LINE公式アカウントを友だち追加したユーザー
- LINE公式アカウントを友だち登録していないが、LINE公式アカウントにメッセージを送ったユーザー（LINE公式アカウントをブロックしているユーザーを除く）
<br><br>

| 必要条件 | 説明 |
| ----------- | ----------- | 
| LINE ビジネスアカウント | このパートナーシップを利用するには、[LINEの公式ビジネスアカウントが必要です](https://www.linebiz.com/jp-en/)。<br><br>LINEメッセージを送信すると、すべてのメッセージがLINE公式アカウントに関連付けられ、ユーザーにはあなたのアカウント名とページが表示されます。|
| メッセージング API チャネル | [LINE公式アカウントマネージャーでメッセージング](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager) APIの使用を有効にすると、メッセージング APIチャネルが作成されます。これは、顧客とのコミュニケーションに使用するチャネルになります。 |
| チャンネルアクセストークン |[チャネルトークン](https://developers.line.biz/en/docs/messaging-api/channel-access-tokens/)を使用すると、LINE公式アカウントを友達として追加したユーザーにメッセージを送信できます。このトークンは、**LINEデベロッパーコンソールのMessaging** **APIタブにあります**。
| ラインユーザー ID | LINEでメッセージを送信するには、' LINE IDs (this ID is different from users'ユーザー（ユーザー名）が必要です。<br><br>ユーザー LINE公式アカウントを友達として追加すると、そのユーザー sers APIにアクセスできるようになります。's LINE ID through LINE' |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:顧客の LINE ID を収集する

LINEでメッセージを送信するには、ユーザーのLINEユーザー名を収集する必要があります。' LINE IDs to identify your user and interact with them consistently. LINE IDs are not the same as the user'LINE IDはLINEによって生成され、LINEのAPIを操作する際に使用できます。

LINE IDは、[LINEユーザーID APIを使用して取得できます](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids)。このエンドポイントは、あなたのLINE公式アカウントを友だちにしたか、あなたのアカウントにメッセージを送信したが、あなたをブロックしていないすべてのユーザーのLINE IDのリストを返します。 

エンドポイントに GET リクエストを行うと`https://api.line.me/v2/bot/followers/ids`、次のようになります。
```json
{
   "userIds":[
      "U4af4980629...",
      "U0c229f96c4...",
      "U95afb1d4df..."
   ],
   "next":"yANU9IA..."
}
```
LINE IDのリストを取得したら、`line_id`それらをカスタム属性としてBrazeに送信します。

### ステップ2:ID をカスタム属性として Braze に送信する

これを調整して開発者と共有し、[カスタム属性として]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes) Braze に送信してください。`line_id`

### ステップ3:チャネルトークンコンテンツブロックとして設定します。

Braze で、\[**テンプレートとメディア] > \[コンテンツブロックライブラリ] > \[+ コンテンツブロックの作成**] に移動し、Braze [コンテンツブロックを作成します]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)。`LINE_Channel_AccessToken`このコンテンツブロックに名前を付けます。 

次に、チャネルトークンコンテンツブロック本体に貼り付けて保存します。

![コンテンツブロック名、Liquidタグ、検閲済みチャネルトークン示すコンテンツブロックの画像, 写真。][2]

コンテンツブロック内でチャネルトークン設定すると、LINE Webhookテンプレートを使用してユーザーにメッセージを送信できるようになります。

### ステップ 4:Webhook テンプレートを選択する

「**テンプレート**」>「**Webhookテンプレート**」に進み、以下のLINE Messenger ウェブフックテンプレートのいずれかを選択します。

![A selection of available predesigned webhook templates.]({% image_buster /assets/img_archive/line_templates.png %}){: style="border:0px;"}

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、\[**エンゲージメント**] > \[**テンプレートとメディア**] > \[**Webhookテンプレート**] に移動します。
{% endalert %}

{% tabs %}
{% tab LINE Text %}
[LINEテキストWebhookテンプレートを使用すると](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)、絵文字をサポートするテキストベースのメッセージを送信できます。

![The line messaging UI with two examples of what a text message will look like on their platform.]({% image_buster /assets/img_archive/line_text_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab LINE Sticker %}
[LINEスタンプテンプレートを使用すると](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)、ステッカーメッセージを送信できます。ステッカーを使用すると、ボットアプリをより表現力豊かでユーザーにとって魅力的なものにすることができます。 

ステッカーを送信するには、メッセージオブジェクトにステッカーのパッケージ ID とステッカー ID を含めてください。Messaging [APIで送信できるステッカーのリストをご覧ください](https://developers.line.biz/en/docs/messaging-api/sticker-list/)。

![The line messaging UI with several examples of what sticker messages look like. These examples include a bear celebrating, a rabbit giving a thumbs up, and a yellow duck.]({% image_buster /assets/img_archive/line_sticker_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab LINE Image %}
[LINE画像](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages), 写真テンプレートを使用すると、LINEユーザーに画像を送信できます。

画像, 写真を送信するには、元の画像と小さいプレビュー画像, 写真の URL をメッセージオブジェクトに含めます。プレビュー画像, 写真がチャットに表示され、画像, 写真をタップすると画像, 写真全体が開きます。URL は HTTPS over TLS 1.2 以降を使用する必要があることに注意してください。

![The line messaging UI showing what an image message will look like on their platform.]({% image_buster /assets/img_archive/line_image_type.png %})
{% endtab %}
{% tab LINE Carousel %}
[LINEカルーセルテンプレートでは](https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template)、複数の列オブジェクトを含むメッセージを送信して、ユーザーが順番に表示することができます。ボタンだけでなく、各列オブジェクトで、ユーザー画像, 写真、タイトル、またはテキスト領域の任意の場所をタップしたときに実行されるアクションを 1 つ指定することもできます。

![The line messaging UI showing a carousel message. This message includes a swipable content box that includes an image, description, a reserve button, and a call button. ]({% image_buster /assets/img_archive/line_carousel_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% endtabs %}

### ステップ 5: Webhook テンプレートセットアップ

Webhook テンプレートにテンプレート名を入力し、必要に応じてチームとタグを追加します。次に、選択したLINEテンプレート種類に応じて、メッセージ、スタンプID、または画像, 写真を入力します。

カスタム属性は、`LINE ID``To:`メッセージ本文のフィールドでテンプレート化する必要があります。そうでない場合は、LINE IDをカスタム属性として含めてください。これは、**Request Body** ボックスの隅にある青と白の + ボタンを使用して実行できます。

#### ウェブフックのプレビューとテスト

メッセージを送信する前に、Webhook をテストしてください。LINE IDがBrazeに保存されていることを確認し（または、見つけてカスタマイズしたユーザーとしてテストし）、プレビューを使用してテストメッセージを送信します。

![Braze Webhook ビルダーの \[テスト] タブには、メッセージを既存のユーザー送信してプレビューできることが表示されます。][3]

メッセージを正常に受信したら、配信設定の設定を開始できます。

## このインテグレーションを使用する

設定が完了したら、このインテグレーションを使用してLINEユーザーをターゲットにします。まず、`LINE ID`カスタム属性として存在するすべてのユーザーのSegment ][62] を作成し、[アナリティクストラッキング] をオンにして [分析ストラッキング] ][61] をオンにして、Messenger のサブスクリプション料金を経時的に追跡します。 

![セグメントフィルター「line_id」が「空白ではない」に設定されています。][63]

Messenger 購読者向けに特定のSegment を作成しない場合は、`LINE ID`エラーを避けるために既存のセグメントを必ず含めてください。

他のキャンペーンと同様に、他のセグメンテーションを使用してLINEキャンペーンやその他のキャンペーン作成プロセスをターゲットにすることもできます。

[1]: {% image_buster /assets/img_archive/line_channel_access_token.png %}
[2]: {% image_buster /assets/img_archive/line_content_block_token.png %}
[3]: {% image_buster /assets/img_archive/line_preview.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/line_segment.png %}
