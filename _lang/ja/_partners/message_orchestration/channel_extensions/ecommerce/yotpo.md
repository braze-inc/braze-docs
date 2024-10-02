---
nav_title: ヨットポ
article_title: ヨットポ
alias: /partners/yotpo/
description: "この参考記事では、BrazeとYotpoのパートナーシップについて概説している。Yotpoはeコマース・マーケティング・プラットフォームのリーディングカンパニーで、何千もの先進的なブランドが消費者直販の成長を加速させるのを支援している。"
page_type: partner
search_tag: Partner
---

# ヨットポ

> 大手eコマース・マーケティング・プラットフォームの[Yotpoは](https://www.yotpo.com/)、何千もの先進的なブランドが消費者直販の成長を加速させるのを支援している。Yotpoのシングルプラットフォームアプローチは、レビュー、ロイヤルティ、SMSマーケティングなどのデータ主導型ソリューションを統合し、ブランドがよりスマートでコンバージョンの高い顧客体験を創造できるようにする。

BrazeとYotpoの統合により、Braze内のEメールやその他のコミュニケーションチャンネルで、商品に関する星評価、トップレビュー、視覚的なユーザー生成コンテンツ（UGC）を動的に取得し、表示することができる。また、顧客レベルのロイヤルティデータをEメールやその他のコミュニケーション手段に含めることで、よりパーソナライズされたインタラクションを実現し、売上とロイヤルティを高めることができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Yotpoアカウント | このパートナーシップを利用するには、Yotpoアカウントが必要である。 |
| YotpoレビューAPIキー | このAPIは、Connected Contentのコード・スニペット内に実装される。<br><br>詳細については、[Yotpoアプリのキーとシークレットキーの見つけ](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key)方を参照のこと。 |
| YotpoロイヤリティAPIキー | このAPIキーとGUIDは、Connected Contentのコード・スニペット内に実装される。<br><br>詳細については、[ロイヤリティ＆リファーラルAPIキーとGUIDを見つけるを](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)参照のこと。|
{: .reset-td-br-1 .reset-td-br-2}

続行する前に、YotpoのプロダクトIDが、Brazeから動的に引き出される`product_id` と同じであることを確認する。これは統合が機能するためには必須である。 

自分のYotpoプロダクトIDを見つけるには、以下のステップを実行する：

1. あなたの店のウェブサイトにアクセスする。
2. 製品ページを開く。
3. 右クリックして**Inspectを**選択する。
4. <kbd>Control</kbd>+<kbd>F</kbd>キーを押し、コード内の`yotpo-main` を検索する。`data-product ID` 変数とその値は、Yotpo divに表示される。

![yotpo-mainを検査して検索し、data-product ID変数を見つける。][1]

## 統合

YotpoとBrazeを統合するには、以下のステップを実行する：

1. Brazeのダッシュボードに行く。
2. **キャンペーン]**ページで\[**キャンペーンを作成]**をクリックし、\[**Eメール]**を選択する。
3. 好みのテンプレートを選択する。
4. **Eメール本文の編集を**クリックし、ユースケースに応じた[コネクテッド・コンテンツ・スニペットを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)追加する：
    - [商品の星評価とレビュー数を表示する](#star-review-count)
    - [製品の最近の5つ星レビューを表示する](#five-star-review)
    - [製品別にビジュアルUGCを表示する](#visual-ugc)
    - [顧客のポイント残高をEメールに表示する](#loyalty-balance)

### 商品の星評価とレビュー数を表示する {#star-review-count}

このスニペットを使って、メールに含まれる商品の公開平均スコアとレビュー総数を提供する：

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}      

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}                    
{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>` をあなたのYotpoレビューAPIキーに置き換える。`product_id` 、Brazeから動的に引き出される。統合が機能するためには、Brazeの`product_id` 、YotpoのプロダクトID（通常はeコマースの親プロダクトID）と一致する必要がある。

![YOTPO-API-KEYをあなたのYotpo Reviews APIキーに置き換える。][2]

### 製品の最近の5つ星レビューを表示する {#five-star-review}

このスニペットを使って、Eメールに含まれる特定の商品のトップ（公表済み）レビューを提供する：

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}              
{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>` をあなたのYotpoレビューAPIキーに置き換える。`product_id` 、Brazeから動的に引き出される。統合が機能するためには、Brazeの`product_id` 、YotpoのプロダクトID（通常はeコマースの親プロダクトID）と一致する必要がある。

メールエディターのスニペットはこんな感じになる：

![最近の5つ星レビューのスニペットを表示するEメールエディターの例][3]

### 製品別にビジュアルUGCを表示する {#visual-ugc}

このスニペットを使って、タグ付けされ公開されたYotpoの画像を取得し、ストック画像の代わりに、または追加のギャラリーとしてメールに追加する：

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product: 

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>` をあなたのYotpoレビューAPIキーに置き換える。`product_id` 、Brazeから動的に引き出される。統合が機能するためには、Brazeの`product_id` 、YotpoのプロダクトID（通常はeコマースの親プロダクトID）と一致する必要がある。

スニペットは次のようになる：

![Yotpoで公開された画像のスニペットを表示するEメールエディタの例][4]

### 顧客のポイント残高をEメールに表示する {#loyalty-balance}

このスニペットを使って、顧客のポイント残高を取得し、Eメールメッセージに使用する：

{% raw %}
```liquid
{% connected_content 

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

`<YOTPO-LOYALTY-GUID>` と`<YOTPO-LOYALTY-API-KEY>` をあなたのYotpoロイヤリティ認証情報に置き換える。`email_address` 、Brazeから動的に引き出される。統合が機能するためには、EメールはEメールを受信する顧客のEメールアドレスでなければならない。

スニペットは次のようになる：

![顧客ロイヤルティ残高のスニペットを表示するEメールエディターの例][5]

## よくある質問 {#faq}

#### もし5つ星のレビューがなかったら？

5つ星のレビューがない場合（エンドポイントのレスポンスが5つ星のレビューに対してNULLを返した場合など）、コンテンツは表示されない。

#### 商品の画像が公開されていない場合は？

商品の画像がない場合（エンドポイントのレスポンスが商品画像に対してNULLを返した場合など）、コンテンツは表示されない。

#### ルック＆フィールをカスタマイズしたり、Yotpoから他のデータフィールドを引き出すことは可能か？

はい、できます。その他のデータ・ポイントやカスタマイズ・オプションについては、[APIコールを行うを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)参照のこと。そのためには、フロントエンド開発者の支援が必要かもしれない。

{% alert note %}
Yotpoはこのガイドに記載されている以上のカスタム要件には対応していない。
{% endalert %}

[1]: {% image_buster /assets/img/yotpo/image1.png %}
[2]: {% image_buster /assets/img/yotpo/image2.png %}
[3]: {% image_buster /assets/img/yotpo/image3.png %}
[4]: {% image_buster /assets/img/yotpo/image4.png %}
[5]: {% image_buster /assets/img/yotpo/image5.png %}