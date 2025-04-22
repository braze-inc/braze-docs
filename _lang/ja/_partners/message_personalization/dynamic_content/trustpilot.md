---
nav_title: トラストパイロット
article_title: トラストパイロット
description: このページでは、Trustpilot とBraze を統合し、レビュー招待を送信し、製品レビューインサイトを使用してメッセージをパーソナライズする方法について説明します。
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# トラストパイロット

> [Trustpilot](https://www.trustpilot.com/)は、顧客がフィードバックを共有し、レビューを管理し、それに対応できるオンラインレビュープラットフォームです。

このページでは、次の手順について説明します。

* Trustpilot のCreate Invitation API を使用したレビュー招待の作成  
* Trustpilot の製品レビューAPI を使用した製品レビューでのメッセージのパーソナライズ

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件 | 説明 |
| --- | --- |
| Trustpilot アカウント | Trustpilot のAPI へのアクセス権を持つTrustpilot アカウントが必要です。 |
| Trustpilot 認証キー | API キーを設定し、アクセストークンをリクエストする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 統合

### ステップ1:Trustpilot API 認証情報を取得する

1. [資格情報を使用してTrustpilot](https://app.contentful.com/login) にログインします。  
2. Trustpilot ダッシュボードでAPI キーとシークレットを作成または取得するには、**Integrations** > **Developers** > **APIs** と移動します。APIキーをまだ持っていない場合は、新規に作成する：  
   1. **Application Name** > **Create Application**に移動します。  
   2. API キーとシークレットをコピーします。これは、接続コンテンツリクエストの認証に使用されます。

## Trustpilot レビュー招待の送信

### ステップ1:Braze Webhook キャンペーンを設定する 

アクションベースのBraze webhook キャンペーンを設定して、Trustpilot API をトリガしてメールレビューの招待状をユーザに送信します。たとえば、ユーザが次のWebhook 詳細を使用して注文した後に、レビュー招待を送信できます。
   * [Webhook URL](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`  
   * 方法:POST  
   * 関連する顧客情報をキーと値のペアとして追加する

### ステップ2:アクセストークンを取得する

1. [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) を使用して、[Trustpilot の認証エンドポイント](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..) に要求してアクセストークンを取得します。
2. **client_credentials** 付与タイプを使用し、API キーとシークレットをConnected Content タグに入力してトークンを取得します。Connected Content リクエストは、リクエストヘッダーに入力できます。接続されたコンテンツは次のようになります。
  
{% raw %}

```liquid
{% connected_content 
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3\.アクセストークンをWebhook キャンペーンのリクエストヘッダーに追加します。

{% alert tip %}
詳細な手順については、[Trustpilot のドキュメント](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites)を参照してください。
{% endalert %}

## 製品レビューインサイトを使用したメッセージのカスタマイズ

Braze キャンペーンで、Trustpilot の[製品レビューサマリーエンドポイント](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary) ({% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}) からデータをリクエストするために、Connected Content コールを実行します。この方法では、ビジネスユニットから特定のSKU の製品レビューを取得します。次の例では、5つ星レビューの特定の製品SKUとフィルタを指定します。

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Liquid を使用して情報を取得するためにメールで接続されたコンテンツ。]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

Connected Contentリクエストは、製品レビューを返します。

{% raw %}
```liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2\.Liquid 構文を使用して、関連するコンテンツをメッセージにプルします。たとえば、製品レビューのコンテンツをプルインするには、Liquid タグ{% raw %}`{{result.productReviews[0].content}}`{% endraw %} を使用します。

![ユーザがカートに残した玩具トラックのレビューを含むパーソナライズされたメール。]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}