---
nav_title: SEEN
article_title: SEEN
description: "この参考記事では、カスタマージャーニーを通じてエンゲージメントを向上させるパーソナライズされた動画をデザインするプラットフォームであるSEENとBrazeのパートナーシップについて概説している。"
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# SEEN

> [SEENは](https://seen.io/)パーソナライゼーション・ビデオ・プラットフォームであり、企業はカスタマーエクスペリエンスをより魅力的にするために、顧客を中心に動画を作成・構築することができる。SEEN を使えば、データを基に動画をデザインし、クラウドで大規模にパーソナライズした後、最適な場所に配信することができます。

## ユースケース

SEENはカスタマージャーニー全体にわたって自動化された動画パーソナライゼーションを提供する。一般的な用途としては、オンボーディング、ロイヤルティ、サインアップとコンバージョン、奪還と解約防止などがあります。

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件          | 説明                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| SEENキャンペーン   | このパートナーシップを利用するには、SEENキャンペーンが必要である。                                                                     |
| データソース   | 動画をパーソナライズするには、SEEN にデータを送る必要があります。Braze ですべての関連データが利用可能であることを確認し、**braze_id** を識別子としてデータを渡します。 |
| Braze Data Transformation Webhook URL   | Braze Data Transformation を使用して、SEEN からの受信データを再フォーマットして、Brazeの /users/track エンドポイントで受け入れられるようにします。 |

## レート制限

SEEN API は現在、1時間に1,000コールを受け入れます。

## SEENとBrazeの統合

以下の例では、動画生成のためにユーザーデータをSEENに送り、配信のためにユニークなランディングページリンクとパーソナライズされたユニークなサムネイルをBrazeに送り返す。この例では、POST Webhookを使用してSEENにデータを送信し、データ変換を使用してBrazeにデータを受信する。SEENで複数の動画キャンペーンを行っている場合は、このプロセスを繰り返してBrazeをすべての動画キャンペーンに接続する。

{% alert tip %}
何か問題が発生した場合は、SEENカスタマーサクセスマネージャーまでご連絡ください。
{% endalert %}

### ステップ1: Webhook キャンペーンの作成

Brazeで新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks)作成する。キャンペーン名をつけ、以下の表を参考にWebhookを作成する：

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>フィールド</strong></th>
      <th><strong>詳細</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Webhook URL</strong></td>
      <td>以下のWebhook URLを使用する。あなたは以下のものを受け取る。 <code>campaign_slug</code> 正しいエンドポイントを呼び出すために、SEEN から受け取ります。<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>HTTPメソッド</strong></td>
      <td>を使用します。 <code>POST</code> メソッド</td>
    </tr>
    <tr>
      <td><strong>Request body</strong></td>
      <td>以下のような生のテキストでリクエスト本文を入力します。<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>詳細については、「<a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">SEEN API</a>」を参照してください。</td>
    </tr>
    <tr>
      <td><strong>リクエストヘッダー</strong></td>
      <td>次の情報を使用して、リクエストヘッダーに入力します。<br><strong>- 認証:</strong><code>Token {token}</code><br><strong>- コンテンツタイプ：</strong><code>application/json</code><br><br>SEEN から認証トークンが届きます。</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Test**タブに切り替えることで、ユーザーを使ってWebhookをテストすることができる。

すべてが意図したとおりに機能したら、Braze に移動し、キャンペーンの送信レートを**毎分10メッセージ**に設定します。こうすれば、SEENのレート制限である1時間あたり1,000コールを超えることはない。

### ステップ2: データ変換を作成する

1. `landing_page_url` と`email_thumbnail_url` の[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)フィールドを新規作成する。これが、この例で使用する2つの属性である。
2. [**データ設定**] で [[データ変換]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites)] を開き、 [**変換の作成**] を選択します。
3. 変換に名前を付けてから、[**ゼロから作成**] を選択し、[**送信先**] を [**POST:ユーザーを追跡] に設定します。ユーザーを追跡** 。
4. [**Webhook の UR Lを SEEN と共有する**] を選択します。
5. 以下のコードを変換の出発点として使うことができる：

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```
{% alert note %}
他のデータも含めたい場合は、それらも含めるようにしてください。コールバックのペイロードに必要なフィールドがすべて含まれるように、SEENとも話し合うことを忘れずに。
{% endalert %}

{: start="6"}
6. 指定されたエンドポイントにテストペイロードを送信する。[SEENドキュメントで](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp)定義されているコールバックペイロードを使いたい場合は、[Postmanや](https://www.postman.com/)他の同様のサービスを使って自分で送信することができる：

```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```

{: start="7"}
7. [**検証**] を選択して、すべてが意図したとおりに動くことを確認すします。
8. [**保存**] および [**アクティブ化する**] を選択します。
