---
nav_title: LINE
article_title: LINE
alias: /partners/line/
description: "この参考文献は、Brazeと、世界中で最も人気のあるインスタントメッセージング プラットフォームの1つであるLINEとの提携について概説している。"
page_type: partner
search_tag: Partner

---

# LINE

> [LINE](https://line.me/en/) は、世界中で最も人気があるインスタントメッセージングプラットフォームの1つであり、1か月あたりのアクティブユーザー数は数億にのぼります。このプラットフォームを通じて、ブランドは豊かで双方向のメッセージングで顧客と関わることができる。

Braze とLINE の統合により、Braze webhook、高度なセグメンテーション、パーソナライゼーション、およびトリガー機能を活用して、[LINE メッセージング API](https://developers.line.biz/en/docs/messaging-api/overview/) を通じてLINE でユーザーにメッセージを送信できます。

## 前提条件

LINE では、ブランドがユーザーの同意を得ている限り、プロモーションメッセージングと非プロモーションメッセージングの両方が可能です。ユーザーにメッセージを送信するには、次の2つの条件のいずれかを満たしている必要があります。
- お客様の LINE 公式アカウントを友だちとして追加したユーザー
- LINEオフィシャルアカウントを友達として追加していないが、LINEオフィシャルアカウントにメッセージを送信したユーザー(LINEオフィシャルアカウントにブロックを行ったユーザーを除く)。
<br><br>

| 要件 | 説明 |
| ----------- | ----------- | 
| LINE ビジネスアカウント | このパートナーシップを活用するには、LINE の[公式ビジネスアカウント](https://www.linebiz.com/jp-en/)が必要です。<br><br>LINE メッセージを送信すると、すべてのメッセージがLINE の公式アカウントに関連付けられ、アカウント名とページがユーザーに表示されます。|
| メッセージングAPI チャネル | メッセージング API をLINE [公式アカウントマネージャー](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager) で使用可能にすると、メッセージング API チャネルが作成されます。これは、顧客とのコミュニケーションに使用するチャネルになります。 |
| チャンネル接続トークンs |[チャネルアクセストークン](https://developers.line.biz/en/docs/messaging-api/channel-access-tokens/)を使用すると、LINEオフィシャルアカウントを友達として追加したユーザーにメッセージを送信できます。このトークンは、**LINE 開発者コンソール** の**メッセージAPI** タブにあります。
| LINE ユーザー ID | LINEでメッセージを送信するには、ユーザーのLINE ID(このIDはユーザーのユーザーの名前とは異なります)が必要になります。<br><br>ユーザーがLINEオフィシャルアカウントを友達として追加すると、LINEのユーザーのAPIを介してユーザーのLINE IDにアクセスできます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:顧客 LINE ID の収集

LINE でメッセージを送信するには、ユーザーを識別し、一貫したやり取りを行うためにユーザーの LINE ID を収集する必要があります。LINE ID は、ユーザーのLINE ユーザーの名前とは異なります。LINE ID は LINE によって生成され、LINE の API とのやり取りで使用できます。

LINE ID は、LINE [User ID API](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids) を使用して取得できます。このエンドポイントは、お客様の LINE 公式アカウントを友だちとして追加したユーザー、またはお客様の LINE アカウントにメッセージを送信しておりお客様をブロックしていないユーザー全員の LINE ID のリストを返します。 

エンドポイント `https://api.line.me/v2/bot/followers/ids` に対して GET リクエストを行うと、次の結果が得られます。
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

Braze に `line_id` を[カスタム属性]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes)として送信するために、開発者とこれを調整して共有します。

### ステップ3:チャネルのアクセストークンをコンテンツブロックとして設定します。

Braze で **\[テンプレートとメディア] > \[コンテンツブロックライブラリ] > \[+ コンテンツブロックを作成]** に移動し、Braze [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)を作成します。このコンテンツブロックの名前は`LINE_Channel_AccessToken` です。 

次に、コンテンツブロックボディにチャネルのアクセストークンを貼り付けて保存します。

![コンテンツブロック名、Liquid タグ、検閲済みチャネルアクセストークンが表示されているコンテンツブロック。][2]

コンテンツブロック内のチャネル接続トークンを設定すると、LINE Webhook テンプレートを使用してユーザーsにメッセージを送信できるようになります。

### ステップ4:Webhook テンプレートを選択

\[**テンプレート**] > \[**Webhook テンプレート**] に移動し、以下の LINE Messenger Webhookテンプレートのいずれかを選択します。

![使用可能な事前に設計されている Webhook テンプレート。]({% image_buster /assets/img_archive/line_templates.png %}){: style="border:0px;"}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Engagement**> **Templates &Media**> **Webフックテンプレート** に移動します。
{% endalert %}

{% tabs %}
{% tab LINE テキスト %}
LINE [text](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)Webhook テンプレートを使用すると、絵文字に対応したテキストベースのメッセージを送信できます。

![テキストメッセージがプラットフォーム上でどのように見えるかを示す2 つのサンプルを含む行メッセージング UI。]({% image_buster /assets/img_archive/line_text_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab ラインステッカー %}
LINE [ステッカー](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)テンプレートでステッカーメッセージを送信できます。ステッカーを使用すると、ボットアプリをより表現力豊かにし、ユーザーに魅力的にすることができます。 

ステッカーを送信するには、ステッカーのパッケージID とステッカーID をメッセージオブジェクトに含めます。Messaging API で送信できる[スタンプのリスト](https://developers.line.biz/en/docs/messaging-api/sticker-list/)を参照してください。

![複数のスタンプメッセージの表示例を示す LINE メッセージング ＵＩ。これらの例は、祝うクマ、親指を立てるウサギ、黄色いアヒルである。]({% image_buster /assets/img_archive/line_sticker_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab LINE 画像 %}
LINE の[画像](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)テンプレートを使用すると、LINE ユーザーに画像を送信できます。

画像を送信するには、元の画像の URL と小さなプレビュー画像の URL をメッセージオブジェクトに組み込みます。プレビュー画像はチャットに表示され、フル画像は画像をタップしたときに表示されます。URL には、HTTPS over TLS 1.2 以降を使用する必要があります。

![プラットフォームでの画像メッセージの表示例を示す LINE メッセージング UI。]({% image_buster /assets/img_archive/line_image_type.png %})
{% endtab %}
{% tab LINE カルーセル %}
LINE [carousel](https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template)テンプレートを使用すると、ユーザー sが循環できる複数の列オブジェクトを含むメッセージを送信できます。ボタンを組み込むだけでなく、各カラムオブジェクトで、ユーザーが画像エリア、タイトルエリア、テキストエリアの中のどこかをタップすると実行される1つのアクションを指定することもできます。

![カルーセルメッセージを示す LINE メッセージング UI。このメッセージのスワイプ可能なコンテンツボックスには、画像、説明、\[Reserve] ボタン、\[Call] ボタンが含まれている。]({% image_buster /assets/img_archive/line_carousel_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% endtabs %}

### ステップ 5: Webhook テンプレートのセットアップ

Webhook テンプレートで、テンプレートの名前を入力し、必要に応じてチームとタグs を追加します。次に、選択した LINE テンプレートの種類に応じて、メッセージ、スタンプ ID、または画像を入力します。

カスタム属性 `LINE ID` は、メッセージ本文の `To:` フィールドでテンプレート化されている必要があります。そうでない場合は、LINE ID をカスタム属性として含めます。これを行うには、**Request Body**ボックスの隅にある青と白の+ボタンを使用します。

#### Webフックのプレビューとテスト

Webhookを確認してから送信してください。LINE ID がBraze に保存されていることを確認し(または、LINE ID を見つけてカスタマイズされたユーザーとしてテストする)、プレビューを使用してテストメッセージを送信します。

![Braze Webhookビルダのテストタブで、既存のユーザーに送信してメッセージをプレビューできることを示します。][3]

メッセージが正常に受信された場合は、配信設定s を設定することができます。

## この統合の使用

設定が完了したら、このインテグレーションを使用してLINE ユーザー s を対象にします。まず、`LINE ID` がカスタム属性として設定されているすべてのユーザーの[セグメントを作成し][62]、[分析トラッキング][61]をオンにして Messenger サブスクリプション率を経時的に追跡します。 

![「is not blank」に設定されてるセグメントフィルター「line_id」。][63]

Messenger サブスクライバー向けの特定のセグメントを作成しない場合は、エラーを避けるために、既存の `LINE ID` のフィルターを必ず含めてください。

他のセグメンテーションを使用して、他のキャンペーンと同様に、LINE キャンペーン s および残りのキャンペーン作成処理を対象にすることもできます。

[1]: {% image_buster /assets/img_archive/line_channel_access_token.png %}
[2]: {% image_buster /assets/img_archive/line_content_block_token.png %}
[3]: {% image_buster /assets/img_archive/line_preview.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/line_segment.png %}
