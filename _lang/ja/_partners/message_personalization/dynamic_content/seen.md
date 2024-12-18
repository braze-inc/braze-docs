---
nav_title: シーン
article_title: シーン
description: "SEENのパーソナライズされた動画は、顧客のカスタマージャーニー全体を通して、企業が比類のないアテンションとエンゲージメントを獲得するのに役立っている。"
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# シーン

> [SEENの](https://seen.io/)パーソナライズされた動画は、顧客のカスタマージャーニー全体を通して、企業が比類のないアテンションとエンゲージメントを獲得するのに役立っている。簡単な3ステップで、SEENで動画をパーソナライズさせる：<br>1\.データを中心に動画をデザインする。<br>2\.クラウドで大規模にパーソナライズされる。<br>3\.最も効果的な場所に配布する。

## ユースケース

SEENはカスタマージャーニー全体にわたって自動化された動画パーソナライゼーションを提供する。一般的な用途としては、オンボーディング、ロイヤルティ、サインアップ／コンバージョン、奪還／アンチチャーンなどがある。

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件          | 説明                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| SEENキャンペーン   | このパートナーシップを利用するには、SEENキャンペーンが必要である。                                                                     |
| データソース   | 動画をパーソナライズさせるためには、SEENにデータを送る必要がある。Brazeですべての関連データが利用可能であることを確認し、**braze_idを**識別子としてデータを渡す。 |
| Braze Data Transformation Webhook URL   | Brazeデータ変換は、SEENからの受信データをBrazeの/users/trackエンドポイントで受け入れられるように再フォーマットするために使用される。 |

## レート制限

SEEN APIは現在、1時間に1000コールを受け付けている。

## SEENとBrazeの統合

以下の例では、動画生成のためにユーザーデータをSEENに送り、配信のためにユニークなランディングページリンクとパーソナライズされたユニークなサムネイルをBrazeに送り返す。この例では、POST Webhookを使用してSEENにデータを送信し、データ変換を使用してBrazeにデータを受信する。SEENで複数の動画キャンペーンを行っている場合は、このプロセスを繰り返してBrazeをすべての動画キャンペーンに接続する。

{% alert tip %}
何か問題が発生した場合は、SEENのカスタマーサクセスマネージャーにご相談いただきたい。
{% endalert %}

### ステップ 1: Webhook キャンペーンの作成

Brazeに新しい[Webhookキャンペーンを](https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks)作成する。キャンペーン名をつけ、以下の表を参考にWebhookを作成する：

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
      <td>以下のWebhook URLを使用する。あなたは以下のものを受け取る。 <code>campaign_slug</code> SEENから正しいエンドポイントを呼び出す。<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>HTTPメソッド</strong></td>
      <td>を使う。 <code>POST</code> というメソッドだ。</td>
    </tr>
    <tr>
      <td><strong>Request body</strong></td>
      <td>以下のような生のテキストでリクエスト本文を入力する。<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>詳細は<a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">SEEN APIを</a>参照のこと。</td>
    </tr>
    <tr>
      <td><strong>リクエストヘッダー</strong></td>
      <td>リクエストヘッダーには以下の情報を記入する：<br><strong>- 認可する：</strong><code>Token {token}</code><br><strong>- コンテンツタイプ：</strong><code>application/json</code><br><br>SEENから認証トークンが届く。</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Test**タブに切り替えることで、ユーザーを使ってWebhookをテストすることができる。

すべてが意図したとおりに動いたら、Brazeに行き、キャンペーンの送信レートを**毎分**10**メッセージに**設定する。これにより、SEENのレート制限である1時間あたり1000コールを超えることはない。

### ステップ 2: データ変換を作成する

1. `landing_page_url` と`email_thumbnail_url` に新しい[カスタム属性](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)フィールドを作成する。これが、この例で使用する2つの属性である。
2. [データ](https://www.braze.com/docs/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) **設定の** [データ変換](https://www.braze.com/docs/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites)ツールを開封し、**変換の作成を**選択する。
3. 変身に名前をつけ、**Start from scratchを**選択し、**送信**先を**POSTに設定する：ユーザーを追跡する** 。
4. **WebhookのURLをSEENと共有するを**選択する。
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
他のデータも含めたい場合は、それらも含めるようにする。コールバックのペイロードに必要なフィールドがすべて含まれるように、SEENとも話し合うことを忘れずに。
{% endalert %}

{: start="6"}
6. 指定されたエンドポイントにテストペイロードを送信する。[SEENのドキュメントで](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp)定義されているコールバックペイロードを使いたい場合は、[Postmanや](https://www.postman.com/)他の同様のサービスを使って自分で送信することができる：

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
7. **Validateを**選択して、すべてが意図したとおりに動くことを確認する。
8. すべてが意図したとおりに動いたら、**「Save**and**Activate**」を選択する。
