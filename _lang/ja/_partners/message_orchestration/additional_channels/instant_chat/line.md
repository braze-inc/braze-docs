---
nav_title: LINE
article_title: LINE
alias: /partners/line/
description: "この参考文献は、Brazeと、世界中で最も人気のあるインスタントメッセージング プラットフォームの1つであるLINEとの提携について概説している。"
page_type: partner
search_tag: Partner

---

# LINE

> [LINE](https://line.me/en/) は、世界中で最も人気のあるインスタントメッセージング プラットフォームs の1 つで、数億の月間アクティブユーザーs によって使用されます。このプラットフォームを通じて、ブランドは豊かで双方向のメッセージングで顧客と関わることができる。

Braze とLINE の統合により、Braze webhook、高度なセグメンテーション、パーソナライゼーション、およびトリガー機能を活用して、[LINE メッセージング API](https://developers.line.biz/en/docs/messaging-api/overview/) を通じてLINE でユーザーにメッセージを送信できます。

## 前提条件

ブランドがユーザーの同意を得ていれば、プロモーションと非プロモーションの両方のメッセージングがSをユーザーすることができます。ユーザーs に送信するには、次の2 つの条件のいずれかを満たす必要があります。
- LINEオフィシャルアカウントを友人として追加したユーザー
- LINEオフィシャルアカウントを友達として追加していないが、LINEオフィシャルアカウントにメッセージを送信したユーザー(LINEオフィシャルアカウントにブロックを行ったユーザーを除く)。
<br><br>

| 要件 | 説明 |
| ----------- | ----------- | 
| LINE ビジネスアカウント | この提携の前倒しタグを行うには、LINE [公式ビジネスアカウント](https://www.linebiz.com/jp-en/)が必要です。<br><br>LINE メッセージを送信すると、すべてのメッセージがLINE の公式アカウントに関連付けられ、アカウント名とページがユーザーに表示されます。|
| メッセージングAPI チャネル | メッセージング API をLINE [公式アカウントマネージャー](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager) で使用可能にすると、メッセージング API チャネルが作成されます。これは、顧客 s との通信に使用するチャネルです。 |
| チャンネル接続トークンs |[チャネルアクセストークン](https://developers.line.biz/en/docs/messaging-api/channel-access-tokens/)を使用すると、LINEオフィシャルアカウントを友達として追加したユーザーにメッセージを送信できます。このトークンは、**LINE 開発者コンソール** の**メッセージAPI** タブにあります。
| LINE ユーザー ID | LINEでメッセージを送信するには、ユーザーのLINE ID(このIDはユーザーのユーザーの名前とは異なります)が必要になります。<br><br>ユーザーがLINEオフィシャルアカウントを友達として追加すると、LINEのユーザーのAPIを介してユーザーのLINE IDにアクセスできます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:顧客 LINE ID の収集

LINEでメッセージを送信するには、ユーザーのLINE IDを収集して、ユーザーを識別し、一貫して対話する必要があります。LINE ID は、ユーザーのLINE ユーザーの名前とは異なります。LINE ID はLINE によって生成され、LINE のAPI と対話するときに使用できます。

LINE ID は、LINE [User ID API](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids) を使用して取得できます。このエンドポイントは、LINE official account に友達であるか、アカウントにメッセージを送信し、ブロックしていないすべてのユーザーのLINE ID のリストを返します。 

エンドポイント `https://api.line.me/v2/bot/followers/ids` に対してGET リクエストを行うと、次のようになります。
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
LINE ID の一覧を取得したら、`line_id` カスタム属性としてBraze に送信します。

### ステップ2:IDをカスタム属性としてBrazeに送信

これを調整して開発者s と共有し、`line_id` を[カスタム属性 s]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes) としてBraze に送信します。

### ステップ3:チャネルのアクセストークンをコンテンツブロックとして設定します。

Braze で、**Templates &Media >Content Blocks Library > + Create Content Block** に移動し、Braze[Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) を作成します。このコンテンツブロックの名前は`LINE_Channel_AccessToken` です。 

次に、コンテンツブロックボディにチャネルのアクセストークンを貼り付けて保存します。

![コンテンツブロックの"画像で、コンテンツブロックの名前、リキッドタグ、および検閲されたチャネルアクセストークンが表示されます。][2]

コンテンツブロック内のチャネル接続トークンを設定すると、LINE Webhook テンプレートを使用してユーザーsにメッセージを送信できるようになります。

### ステップ4:Webhook テンプレートを選択

**テンプレート s** > **Webhook テンプレート s** に移動し、次のLINE Messenger Webhook テンプレートs のいずれかを選択します。

![使用可能な符号付きWebhook テンプレートs.]({% image_buster /assets/img_archive/line_templates.png %})の選択{: style="border:0px;"}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Engagement**> **Templates &Media**> **Webフックテンプレート** に移動します。
{% endalert %}

{% tabs %}
{% tab ラインテキスト %}
LINE [text](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)Webhook テンプレートを使用すると、絵文字に対応したテキストベースのメッセージを送信できます。

![テキストメッセージがプラットフォーム上でどのように見えるかを示す2 つのサンプルを含む行メッセージング UI。]({% image_buster /assets/img_archive/line_text_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab ラインステッカー %}
LINE [ステッカー](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)テンプレートでステッカーメッセージを送信できます。ステッカーを使用すると、ボットアプリをより表現力豊かにし、ユーザーに魅力的にすることができます。 

ステッカーを送信するには、ステッカーのパッケージID とステッカーID をメッセージオブジェクトに含めます。Messaging API で送信できるステッカー のリスト[ を参照してください。

![この行は、ステッカーメッセージがどのように見えるかをいくつか例示したUI をメッセージングします。これらの例には、クマを祝うこと、親指をあげるウサギ、黄色いアヒル]({% image_buster /assets/img_archive/line_sticker_type.png %})が含まれる。{: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab LINE画像 %}
LINE ["画像](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)テンプレートを使用すると、"画像sをLINE ユーザーsに送信できます。

"画像を送信するには、元の"画像のURL とメッセージオブジェクトの小さいプレビュー "画像を含めます。プレビュー "画像はチャットに表示され、フル"画像は"画像がアプリになったときに開封されます。URL は、TLS 1.2 以降のHTTPS を使用する必要があります。

!["画像 がプラットフォーム上でどのように表示されるかを示す行メッセージング。]({% image_buster /assets/img_archive/line_image_type.png %})
{% endtab %}
{% tab ラインカローセル %}
LINE [carousel](https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template)テンプレートを使用すると、ユーザー sが循環できる複数の列オブジェクトを含むメッセージを送信できます。ボタンを持つことに加えて、ユーザーが"画像、タイトル、またはテキストエリアのどこかをたたいたときに実行される単一のアクションを列オブジェクトごとに指定することもできます。

![カルーセルメッセージを示す行メッセージングユーザーインターフェイス。このメッセージには、"画像、説明、予約ボタン、コールボタンを含む切り替え可能なコンテンツボックスが含まれています。]({% image_buster /assets/img_archive/line_carousel_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% endtabs %}

### ステップ 5: Webhook テンプレートのセットアップ

Webhook テンプレートで、テンプレートの名前を入力し、必要に応じてチームとタグs を追加します。次に、選択したLINE テンプレートの種類に応じて、メッセージ、ステッカーID、または"画像を入力します。

カスタム属性`LINE ID` は、メッセージ本文の`To:` フィールドのテンプレートd である必要があります。そうでない場合は、LINE ID をカスタム属性として含めます。これを行うには、**Request Body**ボックスの隅にある青と白の+ボタンを使用します。

#### Webフックのプレビューとテスト

Webhookを確認してから送信してください。LINE ID がBraze に保存されていることを確認し(または、LINE ID を見つけてカスタマイズされたユーザーとしてテストする)、プレビューを使用してテストメッセージを送信します。

![Braze Webhookビルダのテストタブで、既存のユーザーに送信してメッセージをプレビューできることを示します。][3]

メッセージが正常に受信された場合は、配信設定s を設定することができます。

## この統合の使用

設定が完了したら、このインテグレーションを使用してLINE ユーザー s を対象にします。まず、\[`LINE ID` がカスタム属性として存在するすべてのユーザーs に対してSegment][62] を作成し、[分析 "トラッキング][61] をオンにして、Messenger サブスクリプションレートを経時的に追跡します。 

![セグメントフィルター"line_id"を"に設定すると空白"ではありません。][63]

Messenger サブスクライバーs に固有のSegmentを作成しない場合は、エラーs を回避するために、`LINE ID` のフィルターを必ず含めてください。

他のセグメンテーションを使用して、他のキャンペーンと同様に、LINE キャンペーン s および残りのキャンペーン作成処理を対象にすることもできます。

[1]: {% image_buster /assets/img_archive/line_channel_access_token.png %}
[2]: {% image_buster /assets/img_archive/line_content_block_token.png %}
[3]: {% image_buster /assets/img_archive/line_preview.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/line_segment.png %}
